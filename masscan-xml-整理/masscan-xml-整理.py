# -*- encoding:utf-8 -*-
from bs4 import BeautifulSoup


def nmap_xls_res(xml):

    soup = BeautifulSoup(open(xml),features="lxml")
    hosts = soup.find_all('host')

    for num in range(0,len(soup.find_all('host'))):
        print(soup.find_all('host')[num].find_all('address')[0]['addr']+':'+soup.find_all('host')[num].find_all('port')[0]['portid'])
        with open("result.txt", "a") as out_file:
            out_file.write(soup.find_all('host')[num].find_all('address')[0]['addr']+':'+soup.find_all('host')[num].find_all('port')[0]['portid']+"\n")






if __name__ == "__main__":
    nmap_xls_res(r'F:\OneDrive\梦工厂\masscan-xml-整理\s.xml')






