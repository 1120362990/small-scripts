# -*- coding: utf-8 -*-
#此文件用来向数据库中导入资产

import xlrd
import sqlite3

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
		使用状态 = sheet.cell(id,2).value.strip()
		所属业务系统 = sheet.cell(id,3).value.strip()
		公网or内网 = sheet.cell(id,4).value.strip()
		负责部门 = sheet.cell(id,5).value.strip()
		负责人 = sheet.cell(id,6).value.strip()
		负责人电话 = str(sheet.cell(id,7).value).strip()
		负责人邮箱 = sheet.cell(id,8).value.strip()
		科室 = sheet.cell(id,9).value.strip()
		sqlyj = "INSERT INTO %s (ID,IP地址,使用状态,所属业务系统,公网or内网,负责部门,负责人,负责人电话,负责人邮箱,科室) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (table,id,IP地址,使用状态,所属业务系统,公网or内网,负责部门,负责人,负责人电话,负责人邮箱,科室)
		print(sqlyj)
		cursor.execute(sqlyj)
		print("Total:%s Now: %s" % (hangshu,id))
		id = id + 1
	conn.commit()
	conn.close()

#向漏洞统计系统中导入数据
def zichandaoru_xitong(DB,xls,tables):
	conn = sqlite3.connect(DB)
	cursor = conn.cursor()
	#设置要读取的xls
	workbook = xlrd.open_workbook(xls,"r")
	sheet = workbook.sheet_by_name(u'Sheet1')

	#循环遍历xls表，项数据库中写入数据
	id = 1
	hangshu = sheet.nrows-1
	while id < hangshu:
		table = '\''+tables+'\''   #为应对较特殊的表名执行sql时报错，因此把表名用单引号包含起来
		id = int(sheet.cell(id,0).value)
		IP地址 = sheet.cell(id,1).value.strip()
		所属业务系统 = sheet.cell(id,3).value.strip()
		公网or内网 = sheet.cell(id,4).value.strip()
		负责人 = sheet.cell(id,6).value.strip()
		负责人电话 = str(sheet.cell(id,7).value).strip()[:-2]
		负责人邮箱 = sheet.cell(id,8).value.strip()
		科室 = sheet.cell(id,9).value.strip()
		sqlyj = "INSERT INTO %s (id,IPdizhi,yewuxitong,gongneiwang,fuzeren,fuzerendianhua,fuzerenyouxiang,keshi) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');" % (table,id,IP地址,所属业务系统,公网or内网,负责人,负责人电话,负责人邮箱,科室)
		cursor.execute(sqlyj)
		print("Total:%s Now: %s" % (hangshu-1,id))
		id = id + 1
	conn.commit()
	conn.close()

if __name__ == "__main__":
	#用来向正常的漏洞库中导入数据
    zichandaoru_changgui('E:/python/归属查询/hulianwang.db',"E:\\python\\新版绿盟漏洞统计脚本-sqlite\\181221互联网资产更新.xlsx",'资产表-181221')
	#三个参数，依次是   数据库位置   要写入数据库的xls,数据要放在"Sheet1"中   要写入的数据表


	#用来向统计系统中导入数据
	#zichandaoru_xitong('E:/python/DjangoMoon/db.sqlite3',"E:\\python\\新版绿盟漏洞统计脚本-sqlite\\公网IP地址明细.xls",'message_zichanxinxi')