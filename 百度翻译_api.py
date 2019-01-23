#  _*_ coding=utf-8 _*_
# 参考 https://blog.csdn.net/mw_nice/article/details/81910843
import urllib
import random
import hashlib
import http.client
import json

def baidu_translate(content):
    appid = '20151113000005349' #你的appid，此处出自上述的参考链接
    secretKey = 'osubCEzlGjzvw8qdQc41' #你的密钥，此处出自上述的参考链接
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'auto'  #源语言
    toLang = 'zh'    #翻译后的语言
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        a = response.read()#获取返回的内容，原始的是json格式，这里下面几行进行了如下转化 json > string > dict
        print(a.decode())
        print(eval(a.decode()))
        print(eval(a.decode()).get('trans_result')[0].get('dst'))
    except Exception as e:
        print('err:'+str(e))
    finally:
        if httpClient:
            httpClient.close()	
if __name__ == "__main__":
    baidu_translate('customize your pinned repositories')#这里输入要翻译的内容