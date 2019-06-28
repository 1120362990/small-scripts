# -*- encoding:utf-8 -*-
from bs4 import BeautifulSoup
import xlwt


def nmap_xls_res(xml):
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('result')
    n = 0

    soup = BeautifulSoup(open(xml),features="lxml")
    for num in range(0,len(soup.find_all('host'))):
        if soup.find_all('host')[num].find_all('status')[0]['state'] == 'down':
            pass
        else:
            for num2 in range (0,len(soup.find_all('host')[num].find_all('port'))):
                print(str(soup.find_all('host')[num].find_all('address')[0]['addr'])+':'+str(soup.find_all('host')[num].find_all('port')[num2]['portid']),soup.find_all('host')[num].find_all('service')[num2]['name'])
                worksheet.write(n,0, label = str(soup.find_all('host')[num].find_all('address')[0]['addr'])+':'+str(soup.find_all('host')[num].find_all('port')[num2]['portid']))
                worksheet.write(n,1, label = str(soup.find_all('host')[num].find_all('service')[num2]['name']))
                n = n + 1
    workbook.save('result.xls')


if __name__ == "__main__":
    nmap_xls_res(r'F:\OneDrive\梦工厂\nmap-xml-整理\1.xml')






