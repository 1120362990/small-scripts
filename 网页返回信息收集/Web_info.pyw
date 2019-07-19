# -*- coding: utf-8 -*-
import requests
import urllib3
from threading import Thread
from bs4 import BeautifulSoup
import queue,threading
import xlwt

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
lock = threading.Lock()


# 处理所提供的url，处理后为主目录及所有二级目录的形式, 返回 urls
def url_handle(url):
    try:
        if '?' in url:
            url = url[0:url.find('?')]
            url_s = url.split('/')
            urls = []
            l = 2
            url_ss = url_s[0] + '//' + url_s[2] + '/'
            urls.append(url_ss)  # 获取主目录
            while (l < len(url_s) - 1):
                l = l + 1
                url_ss = url_ss + url_s[l] + '/'
                urls.append(url_ss[:-1])  # 获取各个次级目录
            return urls
        else:
            url_s = url.split('/')
            urls = []
            l = 2
            url_ss = url_s[0] + '//' + url_s[2] + '/'
            urls.append(url_ss)  # 获取主目录
            while (l < len(url_s) - 1):
                l = l + 1
                url_ss = url_ss + url_s[l] + '/'
                urls.append(url_ss[:-1])  # 获取各个次级目录
            return urls
    except Exception:
        print('url_handle_error:',url)


#  处理链接主函数，调取 url_handle 处理链接，并去掉/ 和去重
def url(urls_txt):
    urls = []
    with open(urls_txt, 'r', encoding = 'utf-8') as f:
        for line in f:
            url = url_handle(line.strip())
            for u in url:
                if u[-1:] == '/':
                    url = u[:-1]
                    urls.append(url)
                else:
                    urls.append(u)
    urls = list(set(urls))
    return urls


def worker(queue, url_info):
    while True:
        if queue.empty():
            break
        url = queue.get(timeout=0.3)
        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36'}
        try:
            re = requests.get(url, headers=headers,verify=False,timeout=5)
            print(re.status_code,re.headers.get('Content-Length'),re.headers.get('Server'),BeautifulSoup(re.content,"lxml").find_all('title')[0].get_text(),url)
            lock.acquire()
            url_info.append([re.status_code,re.headers.get('Content-Length'),re.headers.get('Server'),BeautifulSoup(re.content,"lxml").find_all('title')[0].get_text(),url])
            lock.release()
        except Exception:
            print('请求连接失败：',url)


def Main(filepath):
    url_info = []#用来存放访问结果，最后输入xls

    urls = url(filepath)

    #设置县城
    if len(urls) < 1000:
        thread_count = len(urls)
    else:
        thread_count = 1000

    threads = []
    queue1 = queue.Queue()
    lock = threading.Lock()

    # 添加队列
    for url1 in urls:
        url1 = url1.strip()
        queue1.put(url1)

    # 启动
    for i in range(thread_count):
        threads.append(Thread(target=worker, args=(queue1, url_info)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # 写入xls
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('UrlStat')
    worksheet.write(0, 0, label='stat')
    worksheet.write(0, 1, label='length')
    worksheet.write(0, 2, label='server')
    worksheet.write(0, 3, label='title')
    worksheet.write(0, 4, label='url')
    for x in range(1,len(url_info)+1):
        worksheet.write(x,0, label = url_info[x-1][0])
        worksheet.write(x,1, label = url_info[x-1][1])
        worksheet.write(x,2, label = url_info[x-1][2])
        worksheet.write(x,3, label = url_info[x-1][3])
        worksheet.write(x,4, label = url_info[x-1][4])
    workbook.save('Result.xls')


if __name__ == "__main__":
    Main(r'F:\urls.txt')
