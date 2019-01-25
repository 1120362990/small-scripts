# -*- coding: utf-8 -*-
#此文件用来向数据库中导入资产

import xlrd
import sqlite3



def creat_table_zichan(DB,table_name):
	conn = sqlite3.connect(DB)
	cursor = conn.cursor()
	sqlyj = '''CREATE TABLE '''+table_name+'''(
   ID INT PRIMARY KEY     NOT NULL,
   IP地址          VARCHAR(50)   NOT NULL,
   系统名称            VARCHAR(50),
   维护科室       VARCHAR(50),
   中心责任人姓名       VARCHAR(50),
   中心责任人邮箱       VARCHAR(50),
   中心责任人电话        VARCHAR(50),
   厂商联系人姓名       VARCHAR(50),
   厂商联系人电话       VARCHAR(50),
   是否部委备案系统       VARCHAR(50),
   定级备案登记       VARCHAR(50)
);'''
	cursor.execute(sqlyj)
	conn.commit()
	conn.close()

def creat_table_loudong(DB,table_name):
	conn = sqlite3.connect(DB)
	cursor = conn.cursor()
	sqlyj = '''CREATE TABLE '''+'\''+table_name+'\''+'''(
ID INTEGER PRIMARY KEY autoincrement NOT NULL,
IP地址          VARCHAR(50)   NOT NULL,
系统名称            VARCHAR(50),
维护科室       VARCHAR(50),
中心责任人姓名       VARCHAR(50),
中心责任人邮箱       VARCHAR(50),
中心责任人电话        VARCHAR(50),
厂商联系人姓名       VARCHAR(50),
厂商联系人电话       VARCHAR(50),
是否部委备案系统       VARCHAR(50),
定级备案登记       VARCHAR(50),
端口 VARCHAR(50),
协议 VARCHAR(50),
服务 VARCHAR(50),
漏洞名称 VARCHAR(50),
漏洞风险值 VARCHAR(50),
风险等级 VARCHAR(50),
服务分类 VARCHAR(50),
应用分类 VARCHAR(50),
系统分类 VARCHAR(50),
威胁分类 VARCHAR(50),
时间分类 VARCHAR(50),
CVE年份分类 VARCHAR(50),
发现日期 VARCHAR(50),
CVE编号 VARCHAR(50),
CNNVD编号 VARCHAR(50),
CNCVE编号 VARCHAR(50),
CNVD编号 VARCHAR(50),
详细描述 VARCHAR(50),
解决办法 VARCHAR(50),
返回信息 VARCHAR(50),
修复情况 VARCHAR(50)
);'''
	cursor.execute(sqlyj)
	conn.commit()
	conn.close()

def zichandaoru_changgui(DB,xls,tables):
	conn = sqlite3.connect(DB)

	cursor = conn.cursor()
	#设置要读取的xls
	workbook = xlrd.open_workbook(xls,"r")
	sheet = workbook.sheet_by_name(u'Sheet1')

	#循环遍历xls表，项数据库中写入数据
	id = 1
	hangshu = sheet.nrows-1
	while id <= hangshu:
		table = '\''+tables+'\'' #为应对较特殊的表名执行sql时报错，因此把表名用单引号包含起来
		id = int(sheet.cell(id,0).value)
		IP地址 = sheet.cell(id,1).value.strip()
		系统名称 = sheet.cell(id,2).value.strip()
		维护科室 = sheet.cell(id,3).value.strip()
		中心责任人姓名 = sheet.cell(id,4).value.strip()
		中心责任人邮箱 = sheet.cell(id,5).value.strip()
		中心责任人电话 = str(sheet.cell(id,6).value).strip()
		厂商联系人姓名 = str(sheet.cell(id,7).value).strip()
		厂商联系人电话 = sheet.cell(id,8).value.strip()
		是否部委备案系统 = str(sheet.cell(id,9).value).strip()
		定级备案登记 = sheet.cell(id,10).value.strip()
		sqlyj = "INSERT INTO %s (ID,IP地址,系统名称,维护科室,中心责任人姓名,中心责任人邮箱,中心责任人电话,厂商联系人姓名,厂商联系人电话,是否部委备案系统,定级备案登记) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (table,id,IP地址,系统名称,维护科室,中心责任人姓名,中心责任人邮箱,中心责任人电话,厂商联系人姓名,厂商联系人电话,是否部委备案系统,定级备案登记)
		print(sqlyj)
		cursor.execute(sqlyj)
		print("Total:%s Now: %s" % (hangshu,id))
		id = id + 1
	conn.commit()
	conn.close()



if __name__ == "__main__":
	pass
	#用来向正常的漏洞库中导入数据
    # zichandaoru_changgui(r'F:/Tong.db',r"F:\资产.xls",'资产_1901')
	#三个参数，依次是   数据库位置   要写入数据库的xls,数据要放在"Sheet1"中   要写入的数据表

	#创建资产数据表
	# creat_table_zichan('F:/Tong.db','资产_1901')#第一个参数是数据库位置，第二个参数为所创建资产表的名称

	#创建漏洞数据表
	# creat_table_loudong('F:/Tong.db','漏洞_1901')