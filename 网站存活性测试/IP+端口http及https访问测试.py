# -*- coding: utf-8 -*-
import threading,queue,sys
import requests

#移除报错
requests.packages.urllib3.disable_warnings()
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
			try:
				url1 = 'http://'+url
				response = requests.get(url1,headers=headers,timeout=15,verify=False).status_code
				if response == 200 or response == 404 or response == 403 or response == 404 or response == 502:
					print(url1 +'	'+str(response))
					f2.write('\n'+url1 +'	'+str(response))
				else:
					url2 = 'https://'+url
					response = requests.get(url2,headers=headers,timeout=15,verify=False).status_code
					print(url2 +'	'+str(response))
					f2.write('\n'+url2 +'	'+str(response))
			except:
				print(url +'	'+'Time out or some Error!')
				f2.write('\n'+url +'	'+'Time out or some Error!')
				continue
def main():
	global f2
	f2 = open('test.txt','w+')
	xujiancedeURL = open("daijianURL.txt","r") #读取所要检测的url列表。就是提供给核心代码区域的参数
	thread_count = 1000  #线程数
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

if __name__ == '__main__':
	main()
