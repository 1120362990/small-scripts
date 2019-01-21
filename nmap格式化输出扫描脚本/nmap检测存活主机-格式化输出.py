# -*- coding:utf-8 -*-
import re
from bs4 import BeautifulSoup
import xlwt
import os

#将 -sn 输出的存活主机整理出来   针对xml文件
def adjust_result(file):
    f = open("Live_IP.txt", "w",encoding='utf-8')
    fopen = open(file, "r")
    line = fopen.readlines()
    num = len(line)
    x = 0
    while x < num:
        if 'state="up"' in line[x]:
            print(re.findall('<address addr="(.*?)" addrtype="ipv4"/>',line[x+1].strip(),flags=0)[0])
            f.write(re.findall('<address addr="(.*?)" addrtype="ipv4"/>',line[x+1].strip(),flags=0)[0]+'\n')
        x = x + 1
    f.close()
    print('Total:'+str(len(open("Live_IP.txt", "r").readlines()))+'个IP。文件创建完成。')
#存活主机测试-遗漏可能超过50%
def nmap_liveip_os(IP):
    os.system(f'nmap -v -sn -PE -n --min-hostgroup 1024 --min-parallelism 1024 {IP} -oX result_liveip.xml')
    adjust_result('result_liveip.xml')
    os.remove('result_liveip.xml')

if __name__ == "__main__":
    nmap_liveip_os(r'192.168.111.0/24')  #以nmap格式输入IP地址即可