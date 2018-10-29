# -*- coding: utf-8 -*-
#  子域名收集后的IP查询.py
import xlrd
import socket
import xlwt
readbook = xlrd.open_workbook("xinxi.xlsx","r")
readsheet = readbook.sheet_by_name(u'Sheet3')
writebook = xlwt.Workbook(encoding = 'ascii')
writesheet = writebook.add_sheet('My Worksheet')
i = 0
while i < readsheet.nrows:
	try:
		print readsheet.cell(i,0).value +'	'+ socket.gethostbyname(readsheet.cell(i,0).value)
		writesheet.write(i, 0, readsheet.cell(i,0).value)
		writesheet.write(i, 1, socket.gethostbyname(readsheet.cell(i,0).value))
		i = i + 1
	except:
		print readsheet.cell(i,0).value +'	'+ 'error'
		writesheet.write(i, 1, 'error')
		i = i + 1
writebook.save('jieguo.xls')












#百度搜索页数  0 10 20 30
#必应是 0 12 26 40 54   大概可以每页加12 
#  https://www.ipip.net/ip.html    IP归属查询
#  python  检测url是否能正常访问    http://www.zuidaima.com/share/3100439662693376.htm
#python  try 例子  https://zhidao.baidu.com/question/84424794.html
#获取网站IP
#import socket
#ip = socket.gethostbyname("www.google.com")

'''
import xlrd
import socket
import xlwt
readbook = xlrd.open_workbook("xinxi.xlsx","r")
readsheet = readbook.sheet_by_name(u'Sheet3')
#writesheet.write(0, 0, 'Unformatted value')
writebook = xlwt.Workbook(encoding = 'ascii')
writesheet = writebook.add_sheet('My Worksheet')
#print readsheet.name,readsheet.nrows,readsheet.ncols
i = 0
while i < readsheet.nrows:
	try:
		#print readsheet.cell(i,0).value +'	'+ socket.gethostbyname(readsheet.cell(i,0).value)
		writesheet.write(i, 0, readsheet.cell(i,0).value)
		writesheet.write(i, 1, socket.gethostbyname(readsheet.cell(i,0).value))
		i = i + 1
	except:
		print readsheet.cell(i,0).value +'	'+ 'error'
		#writesheet.write(i, 0, readsheet.cell(i,0).value)
		writesheet.write(i, 1, 'error')
		i = i + 1
writebook.save('jieguo.xls')
'''
