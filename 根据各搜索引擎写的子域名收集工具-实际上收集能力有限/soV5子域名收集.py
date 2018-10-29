# -*- coding: utf-8 -*-
#  soV5子域名收集.py      该脚本需要改3处
import requests
import re
import os
zhuyuming = 'site:xxxx.com'   
# 联想 -www|apps|start|lesc|solutions|pcsupport|blog|news|psref|support|forums|uataccount|account|tabletstart    |logupload|www3|otp|stores|passport|static
# 金山云  -www|dami|pan|game|bbs|e|ks3|docs|ad|passport|activity|console
shoujigshu = 10
fo = open("foo.txt","a") 
def danyedayin(zhuyuming,changdu):#百度搜索出的单页结果打印
    url='http://www.sov5.cn/search?q='+zhuyuming+'&page='+changdu
    response=requests.get(url).content
    subdomain=re.findall('://(.*?).yxdown.com/',response)   #这里每次都需要改
    i = 0
    while i < len(subdomain):
        #print subdomain[i]
        fo.write(subdomain[i]+'.yxdown.com'+"\n")            #这里每次都需要改
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
zhuyuming = 'site:lenovo.com'
shoujigshu = 10
fo = open("foo.txt","a") 
def danyedayin(zhuyuming,changdu):#百度搜索出的单页结果打印
    url='http://www.sov5.cn/search?q='+zhuyuming+'&page='+changdu
    response=requests.get(url).content
    subdomain=re.findall('<span class="a">(.*?).com/',response)
    i = 0
    while i < len(subdomain):
        #print subdomain[i]
        fo.write(subdomain[i]+'.com'+"\n")
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
'''
