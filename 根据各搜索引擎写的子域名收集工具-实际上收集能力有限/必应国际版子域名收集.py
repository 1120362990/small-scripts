# -*- coding: utf-8 -*-
import requests
import re
import os
zhuyuming = 'xxxx.com'
shoujigshu = 100
fo = open("foo.txt","a") 
def danyedayin(zhuyuming,changdu):#百度搜索出的单页结果打印
    #url='http://www.baidu.com/s?wd=site:'+zhuyuming+'&pn='+changdu
    url='http://cn.bing.com/search?q=site:'+zhuyuming+'&first='+changdu
    response=requests.get(url).content
    subdomain=re.findall('target="_blank" href="https://(.*?)/',response)
    i = 0
    while i < len(subdomain):
        #print subdomain[i]
        fo.write(subdomain[i]+"\n")
        i = i + 1
    return;
o = 0
while o < shoujigshu:
    changdu = str(o+12)
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
