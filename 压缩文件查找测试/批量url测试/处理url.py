# -*- coding: utf-8 -*-
#可提取出burp复制出的链接，中带协议的域名
import threading,queue,sys
import requests
import time
import re
import os
#移除报错
requests.packages.urllib3.disable_warnings()

def tiquyuming():
    outfile = open('yuming_guochnegwnejian.txt', 'w')
    for line in open('piliang.txt'):#要检测的url所放置的位置
        #判断是http还是https协议
        if line[0:5] == 'https':#https协议的情况
            print(line)
            pipei = '//.*?/'
            url = re.findall(pipei,line)
            print('https://'+url[0][2:-1])
            outfile.write('https://'+url[0][2:-1]+'\n')
        else:#http协议的情况
            print(line)
            pipei = '//.*?/'
            url = re.findall(pipei,line)
            print('http://'+url[0][2:-1])
            outfile.write('http://'+url[0][2:-1]+'\n')
    outfile.close()
tiquyuming()   
    
def wnjianqucong():#文件去重
    outfile = open('yuming.txt', 'w') #新的文件
    list_1=[]
    for line in open('yuming_guochnegwnejian.txt'):  #老文件
        tmp = line.strip()
        if tmp not in list_1:
            list_1.append(tmp)
            outfile.write(line)
    outfile.close()
wnjianqucong()

#删除中间文件
os.remove(r'yuming_guochnegwnejian.txt')






