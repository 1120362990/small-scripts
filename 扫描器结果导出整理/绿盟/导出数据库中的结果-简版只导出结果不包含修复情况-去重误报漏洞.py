# -*- coding: utf-8 -*-
import sqlite3
import os
import xlwt
import xlrd

def loudongdaochu_jichu(db_name,table_name):
    #设置要导出的xls格式
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet0 = workbook.add_sheet('各系统漏洞概要')
    worksheet1 = workbook.add_sheet('各系统漏洞详情')

    #sheet各系统漏洞概要 表头
    worksheet0.write(0,0,'科室')
    worksheet0.write(0,1,'负责人')
    worksheet0.write(0,2,'系统')
    worksheet0.write(0,3,'公网or内网')
    worksheet0.write(0,4,'高危漏洞个数')
    worksheet0.write(0,5,'中危漏洞个数')
    worksheet0.write(0,6,'存在漏洞的IP个数')

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

    #设置sqlite数据库
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    biao = '\''+table_name+'\''
    cursor.execute("SELECT distinct 科室,负责人,业务系统,公网or内网 FROM %s" % biao);
    a = cursor.fetchall()
    print(a)#获取存在漏洞的系统的信息
    #     a[p][0]-科室    a[p][1- 负责人    a[p][2]-系统    a[p][3]-公网or内网

    p = 0  #循环打印科室，负责人，系统和公网or内网
    while p < len(a):
        xitong = '\''+a[p][2]+'\''   #设置系统
        gongneiwang = '\''+a[p][3]+'\''   #公网or内网
        #print(xitong)
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[高]' AND 公网or内网 =%s AND (修复情况!='误报' OR 修复情况 IS NULL)" % (biao,xitong,gongneiwang));
        gaowei = cursor.fetchall()#获取高危漏洞
        cursor.execute("SELECT IP地址 FROM %s WHERE 业务系统=%s AND 风险等级='[中]' AND 公网or内网=%s AND (修复情况!='误报' OR 修复情况 IS NULL)"% (biao,xitong,gongneiwang));
        zhongwei = cursor.fetchall()#获取中危漏洞
        print(zhongwei)
        cursor.execute("SELECT distinct IP地址 FROM %s WHERE 业务系统=%s AND 公网or内网=%s AND (修复情况!='误报' OR 修复情况 IS NULL)" % (biao,xitong,gongneiwang));
        ipshuliang = cursor.fetchall()#获取存在漏洞的IP
        print(a[p][0]+'    '+a[p][1]+'    '+a[p][2]+'    '+a[p][3]+'    '+'高危漏洞个数：'+str(len(gaowei))+'    '+'中危漏洞个数：'+str(len(zhongwei))+'    '+'存在漏洞的IP个数：'+str(len(ipshuliang)))
        #向xls中写入相关数据，各系统漏洞概要
        worksheet0.write(p+1,0,a[p][0])
        worksheet0.write(p+1,1,a[p][1])
        worksheet0.write(p+1,2,a[p][2])
        worksheet0.write(p+1,3,a[p][3])
        worksheet0.write(p+1,4,len(gaowei))
        worksheet0.write(p+1,5,len(zhongwei))
        worksheet0.write(p+1,6,len(ipshuliang))
        p = p + 1

    #各系统漏洞详情  写入
    biao = '\''+table_name+'\''
    cursor.execute("SELECT ID FROM %s" % biao);
    m = cursor.fetchall()
    x = 0
    while x < len(m):
        # print(len(m))
        # print(m[x][0])
        cursor.execute("SELECT ID,科室,业务系统,公网or内网,负责人,IP地址,端口,协议,服务,漏洞名称,风险等级,CVE编号,详细描述,解决办法 FROM %s WHERE ID = %s" % (biao,m[x][0]));
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
        x = x + 1

    workbook.save(table_name+'.xls')
    print('统计表创建成功')

if __name__ == "__main__":
    loudongdaochu_jichu('E:/python/归属查询/hulianwang.db','月度漏洞库-181129-公网及内网')
