# -*- encoding:utf-8 -*-
from bs4 import BeautifulSoup
import xlwt


def nmap_xls_res(xml):
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('result')
    n = 0

    soup = BeautifulSoup(open(xml),features="lxml")
    for num in range(0,len(soup.find_all('host'))):
        # print(str(soup.find_all('host')[num].find_all('address')[0]['addr']))  # ip
        # print(soup.find_all('host')[num].find_all('status')[0]['state']) # ip state
        if soup.find_all('host')[num].find_all('status')[0]['state'] == 'up':
            # print(str(soup.find_all('host')[num].find_all('address')[0]['addr']))#ip
            for num2 in range(0,len(soup.find_all('host')[num].find_all('port'))):
                if str(soup.find_all('host')[num].find_all('state')[num2]['state']) == 'open':
                # print(str(soup.find_all('host')[num].find_all('state')[num2]['state']))#port stat
                    # print(str(soup.find_all('host')[num].find_all('address')[0]['addr'])+'	'+str(soup.find_all('host')[num].find_all('port')[num2]['portid'])+'	'+'1')#port
                    try:
                        print(str(soup.find_all('host')[num].find_all('address')[0]['addr'])+'	'+str(soup.find_all('host')[num].find_all('port')[num2]['portid'])+'	'+soup.find_all('host')[num].find_all('service')[num2]['name'])#ip port service
                        worksheet.write(n,0, label = str(soup.find_all('host')[num].find_all('address')[0]['addr']))
                        worksheet.write(n,1, label = str(soup.find_all('host')[num].find_all('port')[num2]['portid']))
                        worksheet.write(n,2, label = str(soup.find_all('host')[num].find_all('service')[num2]['name']))
                        n = n+1
                    except Exception:
                        print(str(soup.find_all('host')[num].find_all('address')[0]['addr'])+'	'+str(soup.find_all('host')[num].find_all('port')[num2]['portid']))#ip port    ,some ip  don't have service name
                        worksheet.write(n,0, label = str(soup.find_all('host')[num].find_all('address')[0]['addr']))
                        worksheet.write(n,1, label = str(soup.find_all('host')[num].find_all('port')[num2]['portid']))
                        n = n+1
                else:
                    pass
        else:
            pass
    workbook.save('result.xls')


if __name__ == "__main__":
    nmap_xls_res(r'F:\1.xml')
