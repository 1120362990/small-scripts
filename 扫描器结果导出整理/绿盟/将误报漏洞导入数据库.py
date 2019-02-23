# -*- coding: utf-8 -*-
import xlrd
import sqlite3
import xlwt
import os
import re

# 得到xls中的所有数据
def get_content_xls(xls,name_sheet):
    workbook = xlrd.open_workbook(xls,"r")
    sheet = workbook.sheet_by_name(u'%s' % name_sheet) 
    vulnlists = []
    for x in range(1,sheet.nrows):
        vulnlist = []
        vulnlist.append(int(sheet.cell(x,0).value))
        vulnlist.append(sheet.cell(x,1).value)
        vulnlist.append(sheet.cell(x,2).value)
        vulnlist.append(sheet.cell(x,3).value)
        vulnlist.append(sheet.cell(x,4).value)
        vulnlist.append(sheet.cell(x,5).value)
        vulnlist.append(sheet.cell(x,6).value)
        vulnlist.append(sheet.cell(x,7).value)
        vulnlist.append(sheet.cell(x,8).value)
        vulnlist.append(sheet.cell(x,9).value)
        vulnlist.append(sheet.cell(x,10).value)
        vulnlist.append(sheet.cell(x,11).value)
        vulnlist.append(sheet.cell(x,12).value)
        vulnlist.append(sheet.cell(x,13).value)
        vulnlist.append(sheet.cell(x,14).value)
        vulnlist.append(sheet.cell(x,15).value)
        vulnlists.append(vulnlist)
    for xx in vulnlists:
        pass
    return vulnlists

#写入数据库
def loudongdaoru_wubao(DB,vulnlists,db_table_name):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    for x in range(0,len(vulnlists)):
        print(x+1,len(vulnlists))  #进度
        科室 = vulnlists[x][1]
        业务系统 = vulnlists[x][2]
        公网or内网 = vulnlists[x][3]
        负责人 = vulnlists[x][4]
        IP地址 = vulnlists[x][5]
        端口 = vulnlists[x][6]
        协议 = vulnlists[x][7]
        服务 = vulnlists[x][8]
        漏洞名称 = vulnlists[x][9]
        风险等级 = vulnlists[x][10]
        CVE编号 = vulnlists[x][11]
        详细描述 = vulnlists[x][12]
        解决办法 = vulnlists[x][13]
        误报原因 = vulnlists[x][14]
        反馈时间 = int(vulnlists[x][15])
        cursor.execute('''INSERT INTO '''+db_table_name+'''(科室,业务系统,公网or内网,负责人,IP地址,端口,协议,服务,漏洞名称,风险等级,CVE编号,详细描述,解决办法,误报原因,反馈时间) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(科室,业务系统,公网or内网,负责人,IP地址,端口,协议,服务,漏洞名称,风险等级,CVE编号,详细描述,解决办法,误报原因,反馈时间))
    conn.commit()
    conn.close()

if __name__ == "__main__":
	#需要已写入四个参数：漏洞数据库文件  要写入的xls文件  漏洞库表  资产表
    vulnlists = get_content_xls(r'F:\误报漏洞-11.xlsx','Sheet1')   #两个参数   存放误报漏洞的xls    误报漏洞所存在的sheet
    loudongdaoru_wubao(r'F:/wang.db',vulnlists,'\'' + '误报漏洞库_190222' + '\'')                 #三个参数    数据库文件    取自上个函数-不用改    存在误报漏洞的数据表