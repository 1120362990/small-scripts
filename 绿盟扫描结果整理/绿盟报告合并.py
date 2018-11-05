# -*- coding: utf-8 -*-
#脚本功能：对绿盟扫描器的主机扫描结果excel版本进行汇总。把文件夹内的多个绿盟主机excel报表中的数据汇总到一个sheet中。


#修改目标，需要支持便携及机架扫描报告。直接针对压缩包进行处理。包含解压、汇总、删除临时文件等

import xlrd
import xlwt
import os

workbook1 = xlwt.Workbook(encoding = 'ascii')
worksheet1 = workbook1.add_sheet('My Worksheet')




ips = open("jieguo.txt","r")#包含要合并的xls的名称，bat脚本能解决，后续会添加功能支持
global duankou
global xieyi
global fuwu
global o 
o = 1
for ip in ips:
	dakaiwenjian = ip.strip()
	workbook = xlrd.open_workbook(dakaiwenjian,"r")
	sheet = workbook.sheet_by_name(r'漏洞信息')
	nrows = sheet.nrows
	i = 0
	while i < nrows:
		print(ip.strip(),sheet.name,sheet.nrows)
		
		duhangshu = 1
		
		while duhangshu < sheet.nrows:
			print('该sheet页行数:'+str(duhangshu))
			print('总sheet页行数:'+str(o))

			if (sheet.cell(duhangshu,0).value == ''):
				worksheet1.write(o, 0, ip[0:-5])
				worksheet1.write(o, 1, duankou)
				worksheet1.write(o, 2, xieyi)
				worksheet1.write(o, 3, fuwu)
				worksheet1.write(o, 4, sheet.cell(duhangshu,3).value)
				worksheet1.write(o, 5, sheet.cell(duhangshu,4).value)
				worksheet1.write(o, 6, sheet.cell(duhangshu,5).value)
				worksheet1.write(o, 7, sheet.cell(duhangshu,6).value)
				worksheet1.write(o, 8, sheet.cell(duhangshu,7).value)
				worksheet1.write(o, 9, sheet.cell(duhangshu,8).value)
				worksheet1.write(o, 10, sheet.cell(duhangshu,9).value)
				worksheet1.write(o, 11, sheet.cell(duhangshu,10).value)
				worksheet1.write(o, 12, sheet.cell(duhangshu,11).value)
				worksheet1.write(o, 13, sheet.cell(duhangshu,12).value)
				worksheet1.write(o, 14, sheet.cell(duhangshu,13).value)
				worksheet1.write(o, 15, sheet.cell(duhangshu,14).value)
				worksheet1.write(o, 16, sheet.cell(duhangshu,15).value)
				worksheet1.write(o, 17, sheet.cell(duhangshu,16).value)
				worksheet1.write(o, 18, sheet.cell(duhangshu,17).value)
				worksheet1.write(o, 19, sheet.cell(duhangshu,18).value)
				worksheet1.write(o, 20, sheet.cell(duhangshu,19).value)
				duhangshu = duhangshu + 1
				o = o +1
			else:
				worksheet1.write(o, 0, ip[0:-5])
				worksheet1.write(o, 1, sheet.cell(duhangshu,0).value)
				worksheet1.write(o, 2, sheet.cell(duhangshu,1).value)
				worksheet1.write(o, 3, sheet.cell(duhangshu,2).value)
				worksheet1.write(o, 4, sheet.cell(duhangshu,3).value)
				worksheet1.write(o, 5, sheet.cell(duhangshu,4).value)
				worksheet1.write(o, 6, sheet.cell(duhangshu,5).value)
				worksheet1.write(o, 7, sheet.cell(duhangshu,6).value)
				worksheet1.write(o, 8, sheet.cell(duhangshu,7).value)
				worksheet1.write(o, 9, sheet.cell(duhangshu,8).value)
				worksheet1.write(o, 10, sheet.cell(duhangshu,9).value)
				worksheet1.write(o, 11, sheet.cell(duhangshu,10).value)
				worksheet1.write(o, 12, sheet.cell(duhangshu,11).value)
				worksheet1.write(o, 13, sheet.cell(duhangshu,12).value)
				worksheet1.write(o, 14, sheet.cell(duhangshu,13).value)
				worksheet1.write(o, 15, sheet.cell(duhangshu,14).value)
				worksheet1.write(o, 16, sheet.cell(duhangshu,15).value)
				worksheet1.write(o, 17, sheet.cell(duhangshu,16).value)
				worksheet1.write(o, 18, sheet.cell(duhangshu,17).value)
				worksheet1.write(o, 19, sheet.cell(duhangshu,18).value)
				worksheet1.write(o, 20, sheet.cell(duhangshu,19).value)
				duankou = sheet.cell(duhangshu,0).value
				xieyi = sheet.cell(duhangshu,1).value
				fuwu = sheet.cell(duhangshu,2).value	
				duhangshu = duhangshu + 1
				o = o +1				
			

		break
worksheet1.write(0, 0, 'IP')
worksheet1.write(0, 1, '端口')
worksheet1.write(0, 2, '协议')
worksheet1.write(0, 3, '服务')
worksheet1.write(0, 4, '漏洞名称')
worksheet1.write(0, 5, '漏洞风险值')
worksheet1.write(0, 6, '风险等级')
worksheet1.write(0, 7, '服务分类')
worksheet1.write(0, 8, '应用分类')
worksheet1.write(0, 9, '系统分类')
worksheet1.write(0, 10, '威胁分类')
worksheet1.write(0, 11, '时间分类')
worksheet1.write(0, 12, 'CVE年份分类')
worksheet1.write(0, 13, '发现日期')
worksheet1.write(0, 14, 'CVE编号')
worksheet1.write(0, 15, 'CNNVD编号')
worksheet1.write(0, 16, 'CNCVE编号')
worksheet1.write(0, 17, 'CNVD编号')
worksheet1.write(0, 18, '详细描述')
worksheet1.write(0, 19, '解决办法')
worksheet1.write(0, 20, '返回信息')
	
workbook1.save('formatting.xls')
