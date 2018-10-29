# -*- coding: utf-8 -*-

import threading,queue,sys
import requests
import time
import re
import os
#移除报错
requests.packages.urllib3.disable_warnings()

def urlstandard():
	outfile = open('foo.txt', 'w')
	for line in open('piliang.txt'):#要检测的url所放置的位置
		reline = line.find('?')
		if reline != -1:
			#print(line[0:reline])#用来去除？后面的参数
			outfile.write(line[0:reline]+'\n')
		else:
			if line[-2:-1] == r'/':#用来除部分目录后面带的/
				#print(line[:-2])
				outfile.write(line[:-2]+'\n')
			else:
				#print(line)
				outfile.write(line+'\n')
	outfile.close()
urlstandard()

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

#旧版结果输出，新版出现问题时可以顶一下。
'''
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
						print('可能存在问题    '+urlx)
						f2.write('\n'+urlx)
					else:
						print(str(r.status_code)+'    '+urlx)
						continue
				except:
					continue
'''
def main():
	global f2
	f2 = open('jieguo.txt','w+')#检测的结果存在这个文件夹里。
	xujiancedeURL = open("jiguoIP.txt","r") #读取所要检测的url列表。就是提供给核心代码区域的参数。要检测的url列表放在这个文件夹里
	
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

	xujiancedeURL.close()
	f2.close()

	os.remove(r'jiguoIP.txt')
	os.remove(r'foo.txt')
if __name__ == '__main__':
	main()






