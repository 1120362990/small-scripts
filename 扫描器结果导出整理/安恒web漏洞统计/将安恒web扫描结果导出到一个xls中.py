# -*- coding: utf-8 -*-
import xlrd
import xlwt
import os

#将某文件夹下的安恒xls报告中的信息输出到一个XLS中
def binalishuchu_anheng():
    XX =1
    workbook_jieguo = xlwt.Workbook(encoding = 'utf-8')
    worksheet0 = workbook_jieguo.add_sheet('漏洞概要')
    #获取所有扫描结果文件名
    file_dir = 'E:\python\新版绿盟漏洞统计脚本-sqlite\web_anheng'    #将要导入的文件发在这个文件夹下
    files = file_name(file_dir)
    worksheet0.write(0,0,'文件路径')            #向xls中写入结果
    worksheet0.write(0,1,'漏洞名称')
    worksheet0.write(0,2,'漏洞名称')
    worksheet0.write(0,3,'漏洞信息')
    worksheet0.write(0,4,'风险等级')
    for file in files:
        xls_name = 'E:\python\新版绿盟漏洞统计脚本-sqlite\web_anheng\\'+file
        workbook = xlrd.open_workbook(xls_name, "r")
        sheet = workbook.sheet_by_name(u'Sheet0')
        x = 169   #从169行开始遍历漏洞
        global loudongmingcheng #声明一个全局便变量来存放漏洞名称
        while sheet.cell(x,0).value != '3 . 参考标准':  #以此标题作为终止遍历的标识
            if sheet.cell(x,0).value[0:6] == '2.1.4.':  #通过匹配序号来得到漏洞名，
                loudongmingcheng = sheet.cell(x,0).value[11:]#提取出漏洞名称赋值给，全局变量 loudongmingcheng
            if sheet.cell(x,0).value == 'URL':
                print(loudongmingcheng)  # 获取漏洞名称，在部分区间获得的是漏洞分类，但不影响输出
                print(sheet.cell(x,1).value)   #URL
                print(sheet.cell(x+1, 1).value)#弱点
                print(sheet.cell(x+2, 1).value)#等级
                worksheet0.write(XX,0,xls_name)            #向xls中写入结果
                worksheet0.write(XX,1,loudongmingcheng)
                worksheet0.write(XX,2,sheet.cell(x,1).value)
                worksheet0.write(XX,3,sheet.cell(x+1, 1).value)
                worksheet0.write(XX,4,sheet.cell(x+2, 1).value)
                XX = XX +1
            x =x+1
    workbook_jieguo.save('anheng_web漏洞统计'+'.xls')
    print('统计表创建成功')


def lm_web_loudongdaoru(xls_name):
    print(xls_name)
    workbook = xlrd.open_workbook(xls_name, "r")
    sheet = workbook.sheet_by_name(u'Web风险分布')
    print(sheet.nrows)  # 打印当前sheet的行数
    x = 2
    while x < sheet.nrows:
        print(sheet.cell(x, 1).value)
        print(sheet.cell(x, 3).value)
        print(sheet.cell(x, 8).value)
        print(sheet.cell(x, 9).value)
        x=x+1

#获取指定文件夹下的文件名称
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return(files)

if __name__ == "__main__":
    binalishuchu_anheng()#这个位置放文件夹吧
    #lm_web_loudongdaoru('http___4.2.134.22_2323_cscf_102_client_%23.xls')






    '''
    x = 'http___4.2.134.22_2323_cscf_102_client_%23.xls'
    print(x[-14:-8])    #判断报告，如果这个值等于  client   那这就是绿盟的报告，如果不是就是安恒
    '''


