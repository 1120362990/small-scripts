# -*- coding: utf-8 -*-
#这个脚本比较特殊，因为360的域名不统一，匹配的是  http://------.com   之间的东西，之后再加上.com
import requests
import re
import os
zhuyuming = 'xxxx.com'
shoujigshu = 64
fo = open("foo.txt","a") 
def danyedayin(zhuyuming,changdu):#搜索出的单页结果打印
    #url='http://www.baidu.com/s?wd=site:'+zhuyuming+'&pn='+changdu
	url='http://www.so.com/s?q=site:'+zhuyuming+'&pn='+changdu
	response=requests.get(url).content
    #subdomain=re.findall('style="text-decoration:none;">(.*?)/',response)
	subdomain=re.findall('<cite>(.*?).com',response)
	i = 0
	while i < len(subdomain):
        #print subdomain[i]
		fo.write(subdomain[i]+"\n")
		i = i + 1
	return;
o = 0
while o < shoujigshu:
    changdu = str(o+1)
    danyedayin(zhuyuming,changdu)
    print str(o)+' page. '+'Total '+str(shoujigshu)+' page.'
    o = o + 1
fo.close()

def wnjianqucong():#文件去重
    outfile = open('jiguoIP.txt', 'w') #新的文件
    list_1=[]
    for line in open('foo.txt'):  #老文件
        tmp = line.strip()
        if tmp not in list_1:
            list_1.append(tmp)
            outfile.write(line)
    outfile.close()
wnjianqucong()

def wnjianhangshu():#获取收集的IP个数 
    filename = "jiguoIP.txt"
    myfile = open(filename)
    lines = len(myfile.readlines())
    myfile.close()
    print "Total found  %s IPS." % (lines)
wnjianhangshu()
os.remove('foo.txt')

#360域名匹配的特殊处理，给域名后面加上  .com
def jiacom():
	f = open("jiguoIP.txt", "r")
	fopen = open("jieguo.txt", "w")
	while True:  
		line = f.readline()  
		if line:  
			line=line.strip()
			p = line +'.com'+ "\n"
			fopen.write( p )
		else:  
			break
	fopen.close()
jiacom()
os.remove('jiguoIP.txt')

#百度搜索页数  0 10 20 30
#必应是 0 12 26 40 54   大概可以每页加12 
#  https://www.ipip.net/ip.html    IP归属查询
#  python  检测url是否能正常访问    http://www.zuidaima.com/share/3100439662693376.htm
#python  try 例子  https://zhidao.baidu.com/question/84424794.html
#获取网站IP
#import socket
#ip = socket.gethostbyname("www.google.com")

'''
import requests
import re
import os
zhuyuming = 'pingan.com'
shoujigshu = 100
fo = open("foo.txt","a") 
def danyedayin(zhuyuming,changdu):#百度搜索出的单页结果打印
    url='http://www.baidu.com/s?wd=site:'+zhuyuming+'&pn='+changdu
    response=requests.get(url).content
    subdomain=re.findall('style="text-decoration:none;">(.*?)/',response)
    i = 0
    while i < len(subdomain):
        #print subdomain[i]
        fo.write(subdomain[i]+"\n")
        i = i + 1
    return;
o = 0
while o < shoujigshu:
    changdu = str(o*10)
    danyedayin(zhuyuming,changdu)
    print str(o)+' page. '+'Total '+str(shoujigshu)+' page.'
    o = o + 1
fo.close()

def wnjianqucong():#文件去重
    outfile = open('jiguoIP.txt', 'w') #新的文件
    list_1=[]
    for line in open('foo.txt'):  #老文件
        tmp = line.strip()
        if tmp not in list_1:
            list_1.append(tmp)
            outfile.write(line)
    outfile.close()
wnjianqucong()

def wnjianhangshu():#获取收集的IP个数 
    filename = "jiguoIP.txt"
    myfile = open(filename)
    lines = len(myfile.readlines())
    lines = lines + 1 
    myfile.close()
    print "Total found  %s IPS." % (lines)
wnjianhangshu()
os.remove('foo.txt')

'''
