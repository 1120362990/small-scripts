# -*- coding: utf-8 -*-

#下一步写IP归属查询

import os
import xlrd
import xlwt
import sqlite3

#获取指定文件夹下的文件名称,   #file_name(os.getcwd())   获取当前文件夹下的文件名
def file_name(file_dir):
	for root, dirs, files in os.walk(file_dir):
		return(files)

#将所有传入的文件名列表中的xls文件，其中端口结果汇总
def duankouhuizong(file_path,files):
	workbook_jieguo = xlwt.Workbook(encoding='utf-8')
	worksheet0 = workbook_jieguo.add_sheet('端口概要')
	worksheet0.write(0, 0, 'IP')  # 向xls中写入结果
	worksheet0.write(0, 1, '端口')
	worksheet0.write(0, 2, '协议')
	worksheet0.write(0, 3, '服务')
	worksheet0.write(0, 4, '状态')
	global XX
	XX = 1
	for xls in files:
		dakaiwenjian = xls.strip()
		workbook = xlrd.open_workbook(file_path+'\\'+dakaiwenjian, "r")
		sheet = workbook.sheet_by_name(r'其它信息')
		nrows = sheet.nrows
		i = 0
		while i < nrows:
			try:
				if (sheet.cell(i, 4).value == 'open'):
					zjIP = workbook.sheet_by_name(r'主机概况')
					worksheet0.write(XX, 0, zjIP.cell(2, 1).value)  # 向xls中写入结果
					worksheet0.write(XX, 1, sheet.cell(i, 1).value)
					worksheet0.write(XX, 2, sheet.cell(i, 2).value)
					worksheet0.write(XX, 3, sheet.cell(i, 3).value)
					worksheet0.write(XX, 4, sheet.cell(i, 4).value)
					XX = XX +1
					i += 1
				else:
					i = i + 1
			except:
				i = i + 1
	workbook_jieguo.save('端口简单统计' + '.xls')
	print('简单统计完成')

#归属查询
def guishuchaxun(DB,zichan_table):
	#读取端口简单统计结果
	workbook = xlrd.open_workbook("端口简单统计.xls", "r")
	sheet = workbook.sheet_by_name(u'端口概要')
	nrows = sheet.nrows
	print(sheet.nrows)
	# 获取数据库连接
	conn = sqlite3.connect(DB)
	cursor = conn.cursor()
	# 创建结果数据表
	workbook = xlwt.Workbook(encoding='ascii')
	worksheet = workbook.add_sheet('My Worksheet')
	# 写入表头
	worksheet.write(0, 0, '科室')
	worksheet.write(0, 1, '负责人')
	worksheet.write(0, 2, '所属业务系统')
	worksheet.write(0, 3, 'IP地址')
	worksheet.write(0, 4, '端口')
	worksheet.write(0, 5, '协议')
	worksheet.write(0, 6, '服务')
	worksheet.write(0, 7, '状态')
	nrow = 1
	m = 1
	while nrow < nrows:
		print(sheet.cell(nrow,0).value)
		cursor.execute("SELECT * FROM '%s' WHERE IP地址 = '%s'" % (zichan_table,sheet.cell(nrow,0).value));
		a = cursor.fetchone()  # 直接像下面那么写报错了，加了个管道好使了
		worksheet.write(m, 3, a[1])  #IP地址
		worksheet.write(m, 2, a[3])  #所属业务系统
		worksheet.write(m, 1, a[6])  #负责人
		worksheet.write(m, 0, a[9])  #科室
		worksheet.write(m, 4, sheet.cell(nrow,1).value)  # 端口
		worksheet.write(m, 5, sheet.cell(nrow,2).value)  # 协议
		worksheet.write(m, 6, sheet.cell(nrow,3).value)  # 服务
		worksheet.write(m, 7, sheet.cell(nrow,4).value)  # 状态
		m = m + 1
		nrow = nrow + 1
	# 关闭数据库连接
	conn.commit()
	conn.close()
	# 保存结果数据表
	workbook.save('各系统端口统计结果.xls')

if __name__ == "__main__":
	xls_path = r'D:\OneDrive\python\绿盟端口统计\190122-互联网中心端口扫描'  #此处填写存放扫描结果的xls的目录
	DB = r'E:/python/归属查询/hulianwang.db'                          #此处填写资产表所在的数据库的位置
	zichan_table = '资产表-181221'                                   #资产表名称

	duankouhuizong(xls_path,file_name(xls_path))
	guishuchaxun(DB,zichan_table)

