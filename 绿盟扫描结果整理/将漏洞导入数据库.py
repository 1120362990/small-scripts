# -*- coding: utf-8 -*-
import xlrd
import sqlite3
import xlwt
import os
import re


#获取指定文件夹下的文件名称++++++++++++++++++++++++++++++++++++++<
def file_name(file_dir):   
	for root, dirs, files in os.walk(file_dir):
		#print(root) #当前目录路径  
		#print(dirs) #当前路径下所有子目录  
		#print(files) #当前路径下所有非目录子文件
		try:
			files.remove('desktop.ini')
		except:
			pass
		return(files)

def lieshu_xls(name_xls,name_sheet):  
	workbook = xlrd.open_workbook(name_xls+".xls","r")    #打开excel文件
	sheet = workbook.sheet_by_name(u'%s' % name_sheet)    #打开特定的sheet页
	return(sheet.ncols)

#将绿盟xls报告中的数据导入数据库中。++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++<
#读取一个excel，先判断是不是便携机，然后将不是便携机的漏洞条目写入到相应的表格中
def loudong_xieru(xls_name,db_table_name,zichan,sheet=r'漏洞信息'):  #xls_name 是去掉.xls的形式，例子：10.68.32.149
	global duankou
	global xieyi
	global fuuw
	
	if lieshu_xls(xls_name,sheet) == 14:#写入便携式扫描器的报告
		print('扫描报告类型：bianixe')
		workbook = xlrd.open_workbook(xls_name+".xls","r")    #打开excel文件
		sheet = workbook.sheet_by_name(u'%s' % sheet)
		#这里做一下xls_name的格式调整，匹配了一下IP
		xls_name = re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",xls_name).group()
		print('操作的xls：'+xls_name)
		print(sheet.nrows)  #行数，实验
		#print(sheet.cell(1,0).value)   #获取表格值，实验
		i = 1
		while i < sheet.nrows:
			print(i)#实验

			#print(sheet.cell(i,5).value)
			if sheet.cell(i,5).value == '[低]':  #去掉漏洞等级为低的漏洞
				print('[低]')
				i = i + 1
			else :
				if (sheet.cell(i,0).value == ''):
					#yaoxierudebiao= db_table_name
					IP地址= xls_name
					print(IP地址)
					端口 = int(duankou)
					协议 = xieyi
					服务 = fuwu
					漏洞名称= sheet.cell(i,3).value#把  ' " \  等的转义问题处理掉
					漏洞风险值= sheet.cell(i,4).value
					风险等级= sheet.cell(i,5).value
					发现日期= sheet.cell(i,6).value
					CVE编号= sheet.cell(i,7).value
					CNNVD编号= sheet.cell(i,8).value
					CNCVE编号= sheet.cell(i,9).value
					CNVD编号= sheet.cell(i,10).value
					详细描述= sheet.cell(i,11).value
					解决办法= sheet.cell(i,12).value
					返回信息= sheet.cell(i,13).value
					cursor.execute('''INSERT INTO '''+db_table_name+''' (IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息))
					#cursor.execute('''INSERT INTO '''+db_table_name+''' (IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息))
					
					#导入科室，业务系统，公网or内网和负责人
					zichan = zichan
					cursor.execute("SELECT * FROM "+ zichan +" WHERE IP地址 = '%s'" % IP地址); 
					a = cursor.fetchone()
					IP地址 ='\''+IP地址+'\''
					try:
						科室 = '\''+a[9]+'\''
						业务系统 = '\''+a[3]+'\''
						公网or内网 = '\''+a[4]+'\''
						负责人 = '\''+a[6]+'\''
					except:
						科室 = '\''+'未查询到相关信息'+'\''
						业务系统 = '\''+'未查询到相关信息'+'\''
						公网or内网 = '\''+'未查询到相关信息'+'\''
						负责人 = '\''+'未查询到相关信息'+'\''
					cursor.execute("UPDATE %s SET 科室 = %s WHERE IP地址 = %s" % (db_table_name,科室,IP地址));
					cursor.execute("UPDATE %s SET 业务系统 = %s WHERE IP地址 = %s" % (db_table_name,业务系统,IP地址));
					cursor.execute("UPDATE %s SET 公网or内网 = %s WHERE IP地址 = %s" % (db_table_name,公网or内网,IP地址));
					cursor.execute("UPDATE %s SET 负责人 = %s WHERE IP地址 = %s" % (db_table_name,负责人,IP地址));


					i = i + 1
				else:
					#yaoxierudebiao= db_table_name
					IP地址= xls_name
					print(IP地址)
					端口= int(sheet.cell(i,0).value)
					协议= sheet.cell(i,1).value
					服务= sheet.cell(i,2).value
					漏洞名称= sheet.cell(i,3).value
					漏洞风险值= sheet.cell(i,4).value
					风险等级= sheet.cell(i,5).value
					发现日期= str(sheet.cell(i,6).value)
					CVE编号= sheet.cell(i,7).value
					CNNVD编号= sheet.cell(i,8).value
					CNCVE编号= sheet.cell(i,9).value
					CNVD编号= sheet.cell(i,10).value
					详细描述= sheet.cell(i,11).value
					解决办法= sheet.cell(i,12).value
					返回信息= sheet.cell(i,13).value
					cursor.execute('''INSERT INTO '''+db_table_name+''' (IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息))
					#cursor.execute('''INSERT INTO '''+db_table_name+''' (IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息))
					#cursor.execute('INSERT INTO "5月漏洞" (ID,服务,漏洞名称,漏洞风险值,风险等级,服务分类,应用分类,系统分类,威胁分类,时间分类,CVE年份分类,发现时间,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息,漏洞状态) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(ID,IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息))
					duankou = 端口
					xieyi = 协议
					fuwu = 服务

					#导入科室，业务系统，公网or内网和负责人
					zichan = zichan
					cursor.execute("SELECT * FROM "+ zichan +" WHERE IP地址 = '%s'" % IP地址); 
					a = cursor.fetchone()
					IP地址 ='\''+IP地址+'\''
					try:
						科室 = '\''+a[9]+'\''
						业务系统 = '\''+a[3]+'\''
						公网or内网 = '\''+a[4]+'\''
						负责人 = '\''+a[6]+'\''
					except:
						科室 = '\''+'未查询到相关信息'+'\''
						业务系统 = '\''+'未查询到相关信息'+'\''
						公网or内网 = '\''+'未查询到相关信息'+'\''
						负责人 = '\''+'未查询到相关信息'+'\''
					cursor.execute("UPDATE %s SET 科室 = %s WHERE IP地址 = %s" % (db_table_name,科室,IP地址));
					cursor.execute("UPDATE %s SET 业务系统 = %s WHERE IP地址 = %s" % (db_table_name,业务系统,IP地址));
					cursor.execute("UPDATE %s SET 公网or内网 = %s WHERE IP地址 = %s" % (db_table_name,公网or内网,IP地址));
					cursor.execute("UPDATE %s SET 负责人 = %s WHERE IP地址 = %s" % (db_table_name,负责人,IP地址));

					i = i + 1
	else:#写入机架式扫描器的报告
		print('jijia')
		print('操作的xls：'+xls_name)
		workbook = xlrd.open_workbook(xls_name+".xls","r")    #打开excel文件
		sheet = workbook.sheet_by_name(u'%s' % sheet)
		print(sheet.nrows)  #行数，实验
		#print(sheet.cell(1,0).value)   #获取表格值，实验
		i = 1
		while i < sheet.nrows:
			print(i)#实验
			#print(sheet.cell(i,5).value)
			if sheet.cell(i,5).value == '[低]':  #去掉漏洞等级为低的漏洞
				print('[低]')
				i = i + 1
			else :
				if (sheet.cell(i,0).value == ''):   
					ID = i
					IP地址=file[0:-4]
					端口= int(duankou)
					协议= xieyi
					服务= fuwu
					漏洞名称= sheet.cell(i,3).value
					漏洞风险值= sheet.cell(i,4).value
					风险等级= sheet.cell(i,5).value
					服务分类= sheet.cell(i,6).value
					应用分类= sheet.cell(i,7).value
					系统分类= sheet.cell(i,8).value
					威胁分类= sheet.cell(i,9).value
					时间分类= sheet.cell(i,10).value
					CVE年份分类= sheet.cell(i,11).value
					发现日期= sheet.cell(i,12).value
					CVE编号= sheet.cell(i,13).value
					CNNVD编号= sheet.cell(i,14).value
					CNCVE编号= sheet.cell(i,15).value
					CNVD编号= sheet.cell(i,16).value
					详细描述= sheet.cell(i,17).value
					解决办法= sheet.cell(i,18).value
					返回信息= sheet.cell(i,19).value
					cursor.execute('''INSERT INTO '''+db_table_name+''' (IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息))

					#导入科室，业务系统，公网or内网和负责人
					zichan = zichan
					cursor.execute("SELECT * FROM "+ zichan +" WHERE IP地址 = '%s'" % IP地址); 
					a = cursor.fetchone()
					IP地址 ='\''+IP地址+'\''
					try:
						科室 = '\''+a[9]+'\''
						业务系统 = '\''+a[3]+'\''
						公网or内网 = '\''+a[4]+'\''
						负责人 = '\''+a[6]+'\''
					except:
						科室 = '\''+'未查询到相关信息'+'\''
						业务系统 = '\''+'未查询到相关信息'+'\''
						公网or内网 = '\''+'未查询到相关信息'+'\''
						负责人 = '\''+'未查询到相关信息'+'\''
					cursor.execute("UPDATE %s SET 科室 = %s WHERE IP地址 = %s" % (db_table_name,科室,IP地址));
					cursor.execute("UPDATE %s SET 业务系统 = %s WHERE IP地址 = %s" % (db_table_name,业务系统,IP地址));
					cursor.execute("UPDATE %s SET 公网or内网 = %s WHERE IP地址 = %s" % (db_table_name,公网or内网,IP地址));
					cursor.execute("UPDATE %s SET 负责人 = %s WHERE IP地址 = %s" % (db_table_name,负责人,IP地址));

					i = i + 1	
				else:
					#yaoxierudebiao= db_table_name
					ID = i 
					IP地址=file[0:-4]
					端口= int(sheet.cell(i,0).value)
					协议= sheet.cell(i,1).value
					服务= sheet.cell(i,2).value
					漏洞名称= sheet.cell(i,3).value
					漏洞风险值= sheet.cell(i,4).value
					风险等级= sheet.cell(i,5).value
					服务分类= sheet.cell(i,6).value
					应用分类= sheet.cell(i,7).value
					系统分类= sheet.cell(i,8).value
					威胁分类= sheet.cell(i,9).value
					时间分类= sheet.cell(i,10).value
					CVE年份分类= sheet.cell(i,11).value
					发现日期= sheet.cell(i,12).value
					CVE编号= sheet.cell(i,13).value
					CNNVD编号= sheet.cell(i,14).value
					CNCVE编号= sheet.cell(i,15).value
					CNVD编号= sheet.cell(i,16).value
					详细描述= sheet.cell(i,17).value
					解决办法= sheet.cell(i,18).value
					返回信息= sheet.cell(i,19).value
					#返回信息= db.escape(sheet.cell(i,19).value) #也是处理 ' " \ " 转义问题的，没上面的号
					cursor.execute('''INSERT INTO '''+db_table_name+''' (IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息))
					duankou = 端口
					xieyi = 协议
					fuwu = 服务

					#导入科室，业务系统，公网or内网和负责人
					zichan = zichan
					print("SELECT * FROM "+ zichan +" WHERE IP地址 = '%s'" % IP地址)
					cursor.execute("SELECT * FROM "+ zichan +" WHERE IP地址 = '%s'" % IP地址); 
					a = cursor.fetchone()
					print(a)
					IP地址 ='\''+IP地址+'\''
					try:
						科室 = '\''+a[9]+'\''
						业务系统 = '\''+a[3]+'\''
						公网or内网 = '\''+a[4]+'\''
						负责人 = '\''+a[6]+'\''
					except:
						科室 = '\''+'未查询到相关信息'+'\''
						业务系统 = '\''+'未查询到相关信息'+'\''
						公网or内网 = '\''+'未查询到相关信息'+'\''
						负责人 = '\''+'未查询到相关信息'+'\''
					cursor.execute("UPDATE %s SET 科室 = %s WHERE IP地址 = %s" % (db_table_name,科室,IP地址));
					cursor.execute("UPDATE %s SET 业务系统 = %s WHERE IP地址 = %s" % (db_table_name,业务系统,IP地址));
					cursor.execute("UPDATE %s SET 公网or内网 = %s WHERE IP地址 = %s" % (db_table_name,公网or内网,IP地址));
					cursor.execute("UPDATE %s SET 负责人 = %s WHERE IP地址 = %s" % (db_table_name,负责人,IP地址));

					i = i + 1
#将绿盟xls报告中的数据导入数据库中。++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>




#将xls报告导入数据库模块++++++++++++++++++++++++++++++++++++++++++++++++++++<重要
def main(DB,xls_dir,yaoxierudebiao,zichan):
	# 连接数据库
	global cursor
	conn = sqlite3.connect(DB)
	cursor = conn.cursor()

	# 获取所有扫描结果文件名
	file_dir = xls_dir  # 将要导入的文件发在这个文件夹下
	files = file_name(file_dir)
	print(files)

	# 循环遍历查询每个IP所归属的系统名,调用写入函数把数据写入到数据库中
	p = 0  # 测试导入表格的数量
	global file
	for file in files:
		print(file[0:-4])
		yaoxierudebiao = yaoxierudebiao
		zichan = zichan
		loudong_xieru('E:\\python\\新版绿盟漏洞统计脚本-sqlite\\ceshi\\' + file[0:-4], yaoxierudebiao,zichan)  # 这里设置要写入的表名，月份
		p = p + 1  # 测试导入表格的数量
		print('已导入' + str(p) + '张数据表')  # 测试导入表格的数量
	conn.commit()
	conn.close()
#将xls报告导入数据库模块++++++++++++++++++++++++++++++++++++++++++++++++++++>




if __name__ == "__main__":
	main('E:/python/归属查询/hulianwang.db','E:\python\新版绿盟漏洞统计脚本-sqlite\ceshi','\'' + '月度漏洞库-1804' + '\'','\'' + '资产表-1804' + '\'')
	#需要已写入四个参数：漏洞数据库文件  要写入的xls文件  漏洞库表  资产表

