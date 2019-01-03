# -*- coding: utf-8 -*-
import sqlite3
import os
import xlwt
import xlrd

def benyuejieguo(Main_DB,tablename):
    #设置要导出的xls格式
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet0 = workbook.add_sheet('各系统本月漏洞现状')
    worksheet1 = workbook.add_sheet('各系统本月漏洞详情')

    #sheet各系统漏洞概要 表头
    #合并所需的单元格，并写入默认数据
    worksheet0.write_merge(0, 0, 0, 10,tablename+'漏洞新发现情况')#  上 下 左 右  写入的内容
    worksheet0.write_merge(1, 2, 0, 0,'科室')
    worksheet0.write_merge(1, 2, 1, 1,'负责人')
    worksheet0.write_merge(1, 2, 2, 2,'系统')
    worksheet0.write_merge(1, 2, 3, 3,'公网or内网')
    worksheet0.write_merge(1,1, 4, 6,'高危漏洞')
    worksheet0.write_merge(1, 1, 7, 9,'中危漏洞')
    worksheet0.write_merge(1, 2, 10, 10,'问题IP数量')
    worksheet0.write(2, 4, '共发现')
    worksheet0.write(2, 5, '新发现')
    worksheet0.write(2, 6, '未修复')
    worksheet0.write(2, 7, '共发现')
    worksheet0.write(2, 8, '新发现')
    worksheet0.write(2, 9, '未修复')

    # #sheet各系统漏洞概要 表头
    # worksheet0.write(0,0,'互联网中心本月漏洞发现情况')
    # worksheet0.write(1,0,'科室')
    # worksheet0.write(1,1,'负责人')
    # worksheet0.write(1,2,'系统')
    # worksheet0.write(1,3,'公网or内网')
    # worksheet0.write(1,4,'高危漏洞')
    # worksheet0.write(1,7,'中危漏洞')
    # worksheet0.write(1, 10, '问题IP数量')
    # worksheet0.write(2, 4, '共发现')
    # worksheet0.write(2, 5, '新发现')
    # worksheet0.write(2, 6, '未修复')
    # worksheet0.write(2, 7, '共发现')
    # worksheet0.write(2, 8, '新发现')
    # worksheet0.write(2, 9, '未修复')

    #sheet各系统漏洞详情 表头
    worksheet1.write(0,0,'ID')
    worksheet1.write(0,1,'科室')
    worksheet1.write(0,2,'业务系统')
    worksheet1.write(0,3,'公网or内网')
    worksheet1.write(0,4,'负责人')
    worksheet1.write(0,5,'IP地址')
    worksheet1.write(0,6,'端口')
    worksheet1.write(0,7,'协议')
    worksheet1.write(0,8,'服务')
    worksheet1.write(0,9,'漏洞名称')
    worksheet1.write(0,10,'风险等级')
    worksheet1.write(0,11,'CVE编号')
    worksheet1.write(0,12,'详细描述')
    worksheet1.write(0,13,'解决办法')
    worksheet1.write(0,14,'修复情况')

    #设置sqlite数据库
    conn = sqlite3.connect(Main_DB)
    cursor = conn.cursor()
    biao = '\''+tablename+'\''
    cursor.execute("SELECT distinct 科室,负责人,业务系统,公网or内网 FROM %s" % biao);
    a = cursor.fetchall()
    print(a)#获取存在漏洞的系统的信息
    #     a[p][0]-科室    a[p][1- 负责人    a[p][2]-系统    a[p][3]-公网or内网

    p = 0  #循环打印科室，负责人，系统和公网or内网
    while p < len(a):
        xitong = '\''+a[p][2]+'\''   #设置系统
        gongneiwang = '\''+a[p][3]+'\''   #公网or内网
        #print(xitong)
        #打印高危漏洞数目
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[高]' AND 公网or内网 =%s" % (biao,xitong,gongneiwang));
        gaowei = cursor.fetchall()#获取高危漏洞
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[中]' AND 公网or内网 =%s" % (biao,xitong,gongneiwang));
        zhongwei = cursor.fetchall()#获取中危漏洞
        cursor.execute("SELECT distinct IP地址 FROM %s WHERE 业务系统=%s AND 公网or内网 =%s" % (biao,xitong,gongneiwang));
        ipshuliang = cursor.fetchall()#获取存在漏洞的IP
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[中]' AND 修复情况='新发现' AND 公网or内网 =%s" % (biao,xitong,gongneiwang));
        xinfaxian_zhong_IP= cursor.fetchall()#获取该系统新发现的中危漏洞
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[中]' AND 修复情况='未修复' AND 公网or内网 =%s" % (biao,xitong,gongneiwang));
        weixiufu_zhong_IP = cursor.fetchall()#获取该系统未修复的中危漏洞
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[高]' AND 修复情况='新发现' AND 公网or内网 =%s" % (biao, xitong,gongneiwang));
        xinfaxian_gao_IP = cursor.fetchall()  # 获取该系统新发现的高危漏洞
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[高]' AND 修复情况='未修复' AND 公网or内网 =%s" % (biao, xitong,gongneiwang));
        weixiufu_gao_IP = cursor.fetchall()  # 获取该系统未修复的高危漏洞


        print(a[p][0]+'    '+a[p][1]+'    '+a[p][2]+'    '+a[p][3]+'    '+'高危漏洞个数：'+str(len(gaowei))+'    '+'中危漏洞个数：'+str(len(zhongwei))+'    '+'存在漏洞的IP个数：'+str(len(ipshuliang)))
        #向xls中写入相关数据，各系统漏洞概要
        worksheet0.write(p+3,0,a[p][0])
        worksheet0.write(p+3,1,a[p][1])
        worksheet0.write(p+3,2,a[p][2])
        worksheet0.write(p+3,3,a[p][3])
        worksheet0.write(p+3,4,len(gaowei))
        worksheet0.write(p + 3, 5, len(xinfaxian_gao_IP))
        worksheet0.write(p + 3, 6, len(weixiufu_gao_IP))
        worksheet0.write(p+3,7,len(zhongwei))
        worksheet0.write(p + 3, 8, len(xinfaxian_zhong_IP))
        worksheet0.write(p + 3, 9, len(weixiufu_zhong_IP))
        worksheet0.write(p+3,10,len(ipshuliang))
        p = p + 1

    #各系统漏洞详情  写入
    biao = '\''+tablename+'\''
    cursor.execute("SELECT ID FROM %s" % biao);
    m = cursor.fetchall()
    x = 0
    while x < len(m):
        print(len(m))
        print(m[x][0])
        cursor.execute("SELECT ID,科室,业务系统,公网or内网,负责人,IP地址,端口,协议,服务,漏洞名称,风险等级,CVE编号,详细描述,解决办法,修复情况 FROM %s WHERE ID = %s" % (biao,m[x][0]));
        xx = cursor.fetchone()
        worksheet1.write(x+1,0,x)
        worksheet1.write(x+1,1,xx[1])
        worksheet1.write(x+1,2,xx[2])
        worksheet1.write(x+1,3,xx[3])
        worksheet1.write(x+1,4,xx[4])
        worksheet1.write(x+1,5,xx[5])
        worksheet1.write(x+1,6,xx[6])
        worksheet1.write(x+1,7,xx[7])
        worksheet1.write(x+1,8,xx[8])
        worksheet1.write(x+1,9,xx[9])
        worksheet1.write(x+1,10,xx[10])
        worksheet1.write(x+1,11,xx[11])
        worksheet1.write(x+1,12,xx[12])
        worksheet1.write(x+1,13,xx[13])
        worksheet1.write(x+1,14,xx[14])
        x = x + 1

    workbook.save(tablename+'漏洞新发现情况统计'+'.xls')
    print('统计表创建成功')


def shangyueqingkuang(Main_DB,tablename):
    #设置要导出的xls格式
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet0 = workbook.add_sheet('各系统上月漏洞修复情况')
    worksheet1 = workbook.add_sheet('各系统上月漏洞修复详情')

    #sheet各系统漏洞概要 表头
    #合并所需的单元格，并写入默认数据
    worksheet0.write_merge(0, 0, 0, 10,tablename+'漏洞修复情况')#  上 下 左 右  写入的内容
    worksheet0.write_merge(1, 2, 0, 0,'科室')
    worksheet0.write_merge(1, 2, 1, 1,'负责人')
    worksheet0.write_merge(1, 2, 2, 2,'系统')
    worksheet0.write_merge(1, 2, 3, 3,'公网or内网')
    worksheet0.write_merge(1,1, 4, 6,'高危漏洞')
    worksheet0.write_merge(1, 1, 7, 9,'中危漏洞')
    worksheet0.write_merge(1, 2, 10, 10,'问题IP数量')
    worksheet0.write(2, 4, '共发现')
    worksheet0.write(2, 5, '已修复')
    worksheet0.write(2, 6, '未修复')
    worksheet0.write(2, 7, '共发现')
    worksheet0.write(2, 8, '已修复')
    worksheet0.write(2, 9, '未修复')

    #sheet各系统漏洞详情 表头
    worksheet1.write(0,0,'ID')
    worksheet1.write(0,1,'科室')
    worksheet1.write(0,2,'业务系统')
    worksheet1.write(0,3,'公网or内网')
    worksheet1.write(0,4,'负责人')
    worksheet1.write(0,5,'IP地址')
    worksheet1.write(0,6,'端口')
    worksheet1.write(0,7,'协议')
    worksheet1.write(0,8,'服务')
    worksheet1.write(0,9,'漏洞名称')
    worksheet1.write(0,10,'风险等级')
    worksheet1.write(0,11,'CVE编号')
    worksheet1.write(0,12,'详细描述')
    worksheet1.write(0,13,'解决办法')
    worksheet1.write(0,14,'修复情况')

    #设置sqlite数据库
    conn = sqlite3.connect(Main_DB)
    cursor = conn.cursor()
    biao = '\''+tablename+'\''
    cursor.execute("SELECT distinct 科室,负责人,业务系统,公网or内网 FROM %s" % biao);
    a = cursor.fetchall()
    print(a)#获取存在漏洞的系统的信息
    #     a[p][0]-科室    a[p][1- 负责人    a[p][2]-系统    a[p][3]-公网or内网

    p = 0  #循环打印科室，负责人，系统和公网or内网
    while p < len(a):
        xitong = '\''+a[p][2]+'\''   #设置系统
        gongneiwang = '\''+a[p][3]+'\''   #公网or内网
        #print(xitong)
        #打印高危漏洞数目
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[高]' AND 公网or内网 =%s AND 修复情况!='误报'" % (biao,xitong,gongneiwang));
        gaowei = cursor.fetchall()#获取高危漏洞
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[中]' AND 公网or内网 =%s AND 修复情况!='误报'" % (biao,xitong,gongneiwang));
        zhongwei = cursor.fetchall()#获取中危漏洞
        cursor.execute("SELECT distinct IP地址 FROM %s WHERE 业务系统=%s AND 公网or内网 =%s AND 修复情况!='误报'" % (biao,xitong,gongneiwang));
        ipshuliang = cursor.fetchall()#获取存在漏洞的IP
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[中]' AND 修复情况='已修复' AND 公网or内网 =%s AND 修复情况!='误报'" % (biao,xitong,gongneiwang));
        yixiufu_zhong_IP= cursor.fetchall()#获取该系统已修复的中危漏洞
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[中]' AND 修复情况='未修复' AND 公网or内网 =%s AND 修复情况!='误报'" % (biao,xitong,gongneiwang));
        weixiufu_zhong_IP = cursor.fetchall()#获取该系统未修复的中危漏洞
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[高]' AND 修复情况='已修复' AND 公网or内网 =%s AND 修复情况!='误报'" % (biao, xitong,gongneiwang));
        yixiufu_gao_IP = cursor.fetchall()  # 获取该系统已修复的高危漏洞
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[高]' AND 修复情况='未修复' AND 公网or内网 =%s AND 修复情况!='误报'" % (biao, xitong,gongneiwang));
        weixiufu_gao_IP = cursor.fetchall()  # 获取该系统未修复的高危漏洞

        print(a[p][0]+'    '+a[p][1]+'    '+a[p][2]+'    '+a[p][3]+'    '+'高危漏洞个数：'+str(len(gaowei))+'    '+'中危漏洞个数：'+str(len(zhongwei))+'    '+'存在漏洞的IP个数：'+str(len(ipshuliang)))
        #向xls中写入相关数据，各系统漏洞概要
        worksheet0.write(p+3,0,a[p][0])
        worksheet0.write(p+3,1,a[p][1])
        worksheet0.write(p+3,2,a[p][2])
        worksheet0.write(p+3,3,a[p][3])
        worksheet0.write(p+3,4,len(gaowei))
        worksheet0.write(p + 3, 5, len(yixiufu_gao_IP))
        worksheet0.write(p + 3, 6, len(weixiufu_gao_IP))
        worksheet0.write(p+3,7,len(zhongwei))
        worksheet0.write(p + 3, 8, len(yixiufu_zhong_IP))
        worksheet0.write(p + 3, 9, len(weixiufu_zhong_IP))
        worksheet0.write(p+3,10,len(ipshuliang))
        p = p + 1

    #各系统漏洞详情  写入
    biao = '\''+tablename+'\''
    cursor.execute("SELECT ID FROM %s" % biao);
    m = cursor.fetchall()
    x = 0
    while x < len(m):
        print(len(m))
        print(m[x][0])
        cursor.execute("SELECT ID,科室,业务系统,公网or内网,负责人,IP地址,端口,协议,服务,漏洞名称,风险等级,CVE编号,详细描述,解决办法,修复情况 FROM %s WHERE ID = %s" % (biao,m[x][0]));
        xx = cursor.fetchone()
        worksheet1.write(x+1,0,x)
        worksheet1.write(x+1,1,xx[1])
        worksheet1.write(x+1,2,xx[2])
        worksheet1.write(x+1,3,xx[3])
        worksheet1.write(x+1,4,xx[4])
        worksheet1.write(x+1,5,xx[5])
        worksheet1.write(x+1,6,xx[6])
        worksheet1.write(x+1,7,xx[7])
        worksheet1.write(x+1,8,xx[8])
        worksheet1.write(x+1,9,xx[9])
        worksheet1.write(x+1,10,xx[10])
        worksheet1.write(x+1,11,xx[11])
        worksheet1.write(x+1,12,xx[12])
        worksheet1.write(x+1,13,xx[13])
        worksheet1.write(x+1,14,xx[14])
        x = x + 1


    workbook.save(tablename+'漏洞修复情况统计'+'.xls')
    print('统计表创建成功')

if __name__ == "__main__":
    #视后续脚本编写进度，考虑是否把xls操作放进主函数里
    #benyuejieguo('E:\\python\\归属查询\\hulianwang.db',"临时漏洞库-181206-省公司漏洞扫描复测")#两个参数依次是： 数据库  想要导出结果的数据表-本月新扫描出的结果，对比后的      导出本月结果
    shangyueqingkuang('E:\\python\\归属查询\\hulianwang.db',"月度漏洞库-181129-公网及内网")#两个参数依次是： 数据库  想要导出结果的数据表-上月结果，对比后的      导出上月漏洞修复情况

