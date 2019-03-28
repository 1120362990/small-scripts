# -*- coding: utf-8 -*-
import urllib3
import threading,queue,sys
import requests
import time
import re
import os
#移除报错
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def neirongtianjia_hou_txt(yuanwenjian):
    urls = []
    f = open(yuanwenjian,"r")
    lines = f.readlines()
    for line in lines:
        # print(line.strip())
        urls.append(line.strip())
    
    #去除?后面的参数
    for url in urls:
        if '?' in url:
            # print(url)
            urls.append(url[:url.find('?')])
            urls.remove(url)
            pass
    for url in urls:
        if '?' in url:
            # print(url)
            urls.append(url[:url.find('?')])
            urls.remove(url)
            pass

    #去除最后的 /
    for url in urls:
        if url[-1] == '/':
            urls.append(url[:-1])
            urls.remove(url)
    for url in urls:
        if url[-1] == '/':
            urls.append(url[:-1])
            urls.remove(url)

    #去重
    urls = list(set(urls))

    # for url in urls:
    #     print(url)
    return urls

#后缀名仓库
suffixs = ('.001','.002','.1','.2','.7z','.arj','.back','.backup','.bak','.bakup','.bas','.bz2','.c','.cab','.conf','.copia',
'.core','.cpp','.dat','.db','.default','.dll','.doc','.gz','.ini',
'.jar','.java','.metalink','.old','.orig','.pas','.rar','.sav','.saved','.source','.src','.stackdump','.tar','.tar.gz',
'.tar.gz.metalink','.temp','.test','.tgz','.tmp','.txt','.war','.Z','.zip','.uue','.iso','.7-zip','.ace','.lzh','.gzip')



class RedisUN(threading.Thread):
	def __init__(self,queue1):
		threading.Thread.__init__(self)
		self._queue = queue1
	def run(self):
		while True:
			if self._queue.empty():
				break
			#实际工作的代码区域
			headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
			url = self._queue.get(timeout=0.5)

			for suffix in suffixs:
				urlx = url + suffix
				try:
					r = requests.get(urlx,headers=headers,verify=False,allow_redirects=False)#https认证关闭，用来访问https协议的网站。关闭重定向，避免因重定向产生的问题。
					if str(r.status_code) == str(200):
						print('Content-Length:'+r.headers.get('Content-Length')+'   '+'可能存在问题    '+urlx)
						f2.write('\n'+'Content-Length:'+'	'+r.headers.get('Content-Length')+'   '+'可能存在问题'+'	'+urlx)
					else:
						print('Content-Length:'+str(r.headers.get('Content-Length'))+'   '+'someerror    '+urlx)
						continue
				except:
					continue


def main():
	global f2
	f2 = open('jieguo.txt','w+')#检测的结果存在这个文件夹里。
	# xujiancedeURL = open("jiguoIP.txt","r") #读取所要检测的url列表。就是提供给核心代码区域的参数。要检测的url列表放在这个文件夹里
	
	xujiancedeURL = neirongtianjia_hou_txt('url.txt')#burp导出的url列表放在这里

	thread_count = 100 #线程数
	threads = []
	queue1 = queue.Queue()

	for line in xujiancedeURL:
		line = line.strip('\n').strip('\ufeff')   #读取每一行
		queue1.put(line)
		
	for i in range(thread_count):
		threads.append(RedisUN(queue1))
	for t in threads:
		t.start()
	for t in threads:
		t.join()

	# xujiancedeURL.close()
	f2.close()


if __name__ == '__main__':
	main()






