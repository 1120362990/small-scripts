# -*- coding: utf-8 -*-
#检测网站是否可访问.py
import requests
import xlwt
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
xujiancedeURL = open("daijianURL.txt","r") 

writebook = xlwt.Workbook(encoding = 'ascii')
writesheet = writebook.add_sheet('My Worksheet')
global i
i = 0
for line in xujiancedeURL:
	line = line.strip('\n').strip('\ufeff')
	url = line
	#print url
	try:
		response = requests.get(url,headers=headers,timeout=15).status_code
		print url +'	'+str(response)
		writesheet.write(i, 0, url)
		writesheet.write(i, 1, response)
		i = i + 1
	except:
		print url +'	'+'Time out or some Error!'
		writesheet.write(i, 0, url)
		writesheet.write(i, 1, 'Time out or some Error!')
		i = i + 1
		
writebook.save('jieguo.xls')	
xujiancedeURL.close()
