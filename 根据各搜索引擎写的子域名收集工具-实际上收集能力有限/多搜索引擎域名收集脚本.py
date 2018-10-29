# -*- coding: utf-8 -*-
import requests
import re
import os
from multiprocessing import Process, Pool
import xlrd
import socket
import xlwt


def soushuo_360(domain):
    shoujiyeshu = 64#s一共收集的页数，360一共可获取64页
    fo = open("360.txt","a")#结果写入的文本文件
    def danyedayin(domain,changdu):
        url = "https://www.so.com/s"#访问的URL
        payload = {'q':'site:'+domain,'pn':changdu}#URL中附带的参数
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
        'Accept':'*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'Connection':'close'}
        res = requests.get(url,params=payload,headers=headers)#发送http请求
        res.encoding="utf-8"
        #print(res.text)#用来获取网页内容
        subdomain=re.findall('class="mingpian" data-h="(.*?)"',res.text)#用正则匹配出页面中所有的域名
        i = 0#循环打印出上面一条语句中匹配到的所有域名
        while i < len(subdomain):
            print("360:"+subdomain[i])
            fo.write(subdomain[i]+"\n")#向文件中写入所匹配到的域名
            i = i + 1
        return
    o = 0#循环打印每一页中的所有参数
    while o <= shoujiyeshu:
        changdu = str(o+1)
        danyedayin(domain,changdu)
        print("360: "+str(o)+' page. '+'Total '+str(shoujiyeshu)+' page.')
        o = o + 1
    fo.close()

def soushuo_baidu(domain):
    shoujiyeshu = 70
    fo = open("baidu.txt","a") 
    def danyedayin(domain,changdu):#百度搜索出的单页结果打印
        url='http://www.baidu.com/s'
        payload = {'wd':'site:'+domain,'pn':changdu}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
        'Accept':'*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'Connection':'close'}
        res = requests.get(url,params=payload,headers=headers)
        res.encoding="utf-8"
        subdomain=re.findall('class="c-showurl" style="text-decoration:none;">(.*?)&nbsp;</a>',res.text)
        i = 0#因为百度匹配出的域名格式不统一，所以做了特殊的处理
        while i < len(subdomain):
            if subdomain[i][:4] == 'http':
                print("baidu: "+re.findall('//(.*?)/',subdomain[i])[0])
                fo.write(re.findall('//(.*?)/',subdomain[i])[0]+"\n")
            else:
                print("baidu: "+re.findall('^(.*?)/',subdomain[i])[0])
                fo.write(re.findall('^(.*?)/',subdomain[i])[0]+"\n")
            i = i + 1
        return
    o = 0
    while o < shoujiyeshu:
        changdu = str(o*10)
        danyedayin(domain,changdu)
        print("baidu: "+str(o)+' page. '+'Total '+str(shoujiyeshu)+' page.')
        o = o + 1
    fo.close()

#必应爬取域名需要cookie的支持，暂时设置了一个固定的cookie，要是有实效==失效机制，还是写一个直接获取cookie的方法吧
def soushuo_biying(domain):
    shoujiyeshu = 700
    fo = open("biying.txt","a")
    def danyedayin(zhuyuming,changdu,FROM):
        url='https://cn.bing.com/search'
        payload = {'q':'site:'+domain,'first':changdu,'FROM':'PERE'+str(FROM)}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'Referer':'https://cn.bing.com/',
        'Host':'cn.bing.com',
        'Cookie':'SNRHOP=I=&TS=; _EDGE_S=F=1&SID=07AB2A12B82C66F03AC6262BB90267B7; _EDGE_V=1; MUID=2EB8F2938A7E619638E6FEAA8B5060C5; MUIDB=2EB8F2938A7E619638E6FEAA8B5060C5; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=7D3B85C0210D4343A1FEBEB5624F4513&dmnchg=1; SRCHUSR=DOB=20180727&T=1532675050000; _SS=SID=07AB2A12B82C66F03AC6262BB90267B7&HV=1532676422; SRCHHPGUSR=CW=1903&CH=947&DPR=1&UTC=480&WTS=63668271792; ipv6=hit=1532678592969&t=4; BFB=ARB2VWb8yoK--aAHZEP4f-hHTE_-MjhViHq7WqM_82bb8A; ClarityID=642574541059451895dd5ddc091dead2',
        'DNT':'1',
        'Upgrade-Insecure-Requests':'1',
        'Connection':'close'}
        res = requests.get(url,params=payload,headers=headers)
        print(res.url)
        res.encoding="utf-8"
        subdomain=re.findall('<a target="_blank" href="(.*?)" h="ID=SERP',res.text)
        i = 0#循环打印出上面一条语句中匹配到的所有域名
        while i < len(subdomain):
            print("biying: "+re.findall('//(.*?)/',subdomain[i])[0])
            fo.write(re.findall('//(.*?)/',subdomain[i])[0]+"\n")#向文件中写入所匹配到的域名
            i = i + 1
        return
    o = 0#循环打印每一页中的所有参数
    i = 1
    while o <= shoujiyeshu:
        changdu = str(o)
        danyedayin(domain,changdu,i)
        print("biying: "+str(o)+' page. '+'Total '+str(shoujiyeshu)+' page.')
        o = o + 10
        i = i + 1
    fo.close()

def wnjianqucong(filename):#文件去重
    outfile = open(filename+'_linshi.txt', 'w') #新的文件
    list_1=[]
    for line in open(filename+'.txt'):  #老文件
        tmp = line.strip()
        if tmp not in list_1:
            list_1.append(tmp)
            outfile.write(line)
    outfile.close()

def wenjianhangshu(filename):#获取文件行数
    filename1 = filename+"_linshi.txt"
    myfile = open(filename1) 
    lines = len(myfile.readlines()) 
    print("%s共发现%s个子域名。" % (filename,lines))

#查询txt中的域名IP地址，并写入xls中
def IPchaxun(filename):
    writebook = xlwt.Workbook(encoding = 'ascii')
    writesheet = writebook.add_sheet('My Worksheet')
    i = 0
    for line in open(filename):
        #print(line.strip())
        try:
            #print(line.strip() +'	'+ socket.gethostbyname(line.strip()))
            writesheet.write(i, 0, line.strip())
            writesheet.write(i, 1, socket.gethostbyname(line.strip()))
            i = i + 1
        except:
            #print(line.strip() +'	'+ 'error')
            writesheet.write(i, 1, 'error')
            i = i + 1
    writebook.save('jieguo.xls')
    print("IP查询完成。")



if __name__ == "__main__":
     
    domain = input('请输入域名:')
    print(domain)
    
    #360收搜收集子域名，这个会把收集到的域名都写入到360.txt中，没去重的版本
    jinchneg_360 = Process(target=soushuo_360, args=(domain,)) 
    jinchneg_360.daemon = True  #防止僵尸进程，确保在父进程结束时，子进程也结束
    jinchneg_360.start()        #开启一个进程
    #baidu收搜收集子域名，这个会把收集到的域名都写入到baidu.txt中，没去重的版本
    jinchneg_baidu = Process(target=soushuo_baidu, args=(domain,)) 
    jinchneg_baidu.daemon = True  #防止僵尸进程，确保在父进程结束时，子进程也结束
    jinchneg_baidu.start()        #开启一个进程
    #360收搜收集子域名，这个会把收集到的域名都写入到biying.txt中，没去重的版本
    jinchneg_biying = Process(target=soushuo_biying, args=(domain,)) 
    jinchneg_biying.daemon = True  #防止僵尸进程，确保在父进程结束时，子进程也结束
    jinchneg_biying.start()        #开启一个进程

    jinchneg_baidu.join()   #join的作用是，子进程结束后再接着执行父进程，在这个位置等待子进程结束后，父进程接下来的代码才会急需执行
    jinchneg_360.join()     #join的作用是，子进程结束后再接着执行父进程，在这个位置等待子进程结束后，父进程接下来的代码才会急需执行
    jinchneg_biying.join()  #join的作用是，子进程结束后再接着执行父进程，在这个位置等待子进程结束后，父进程接下来的代码才会急需执行 
    
    #各个引擎结果去重,合并然后再去从
    soushuoyinqings = {'360','biying','baidu'}
    for soushuoyinqing in soushuoyinqings:
        wnjianqucong(soushuoyinqing)
        wenjianhangshu(soushuoyinqing)
    os.system("type 360_linshi.txt,baidu_linshi.txt,biying_linshi.txt > zhonghe.txt")#文件合并
    wnjianqucong("zhonghe")
    wenjianhangshu("zhonghe")
    


    IPchaxun('zhonghe_linshi.txt')

    soushuoyinqingss = {'360','biying','baidu','zhonghe'}
    #删除中间的文件
    for soushuoyinqing in soushuoyinqingss:
        os.remove(soushuoyinqing+'.txt')
        os.remove(soushuoyinqing+'_linshi.txt')