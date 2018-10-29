# -*- coding: utf-8 -*-
import requests
import re
import os


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
