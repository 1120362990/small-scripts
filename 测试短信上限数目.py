# -*- coding: utf-8 -*-
import requests
import time

#移除报错
requests.packages.urllib3.disable_warnings()



#https  ------------------------get
daunxintiaoshu = 36
i = 0
while i < daunxintiaoshu:
    time.sleep(65)
    print(i)
    #输出系统当前时间
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    data= {
        'mobile':'BPme9ji6G8J2o6a5QcWpIkn+WltcdfgpI8NBuXOC2EslnZVTAOzRpNrKqF0uiBASEPrCoL+5e6ittgkifLEVP6uHw9ZaQOUoUcQSn72LdD29OvUE4/8/Y9D2CJpn26IoFeE4zm0b2clWnr2X7hdWSx3qvuUWwkEXgZ7sY63M45I='
    }
    url = 'https://www.xxx.com/sendSMS'
    headers = {
        'Host': 'item.ln139.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://item.ln139.cn/wskh/rzkNewMain?AD_ID=ff80808161e3f1b90161e45b948a1c57&ORG_ID=17000000&USER_ID=ff8080815e2e866d015e332d6a6a51d9&SHOP_ID=ff8080815e2e866d015e332d6a8751db&_sid_=8be2f279-eb91-4d23-801d-11b86ddb46bf',
        'Content-Length': '189',
	    'Cookie': 'JSESSIONID=4E6B99280C7EBE0DC8C0CB48AFEDFDB4; U_C_VS=',
        'Connection': 'close'
        }
    r = requests.post(url, data=data,headers=headers, verify=False)
    print(r.text)
    print('----------------------------------------------------------------')
    i = i + 1



