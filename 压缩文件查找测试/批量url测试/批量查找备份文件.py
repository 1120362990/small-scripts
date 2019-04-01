# -*- coding: utf-8 -*-
import urllib3
import requests
import threading
import queue

# 移除报错
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def neirongtianjia_hou_txt(yuanwenjian):
    urls = []
    f = open(yuanwenjian, "r")
    lines = f.readlines()
    for line in lines:
        # print(line.strip())
        urls.append(line.strip())

    # 去除?后面的参数
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

    # 去除最后的 /
    for url in urls:
        if url[-1] == '/':
            urls.append(url[:-1])
            urls.remove(url)
    for url in urls:
        if url[-1] == '/':
            urls.append(url[:-1])
            urls.remove(url)

    # 分割多级url
    urls_1 = []
    for url in urls:
        dict = url.split('/')
        url_1 = dict[0]+'//'+dict[2]
        # urls_1.append(url_1)  # 无目录的域名
        i = 3
        while i < len(dict):
            # 通过判断url中都有什么特征值来进行相关的处理
            # 将最后一级目录中带有.的目录去掉,有什么奇怪的目录都可以用这个过滤掉
            if '.' in dict[i] or '*' in dict[i]:
                pass
            else:
                url_1 = url_1 + '/' + dict[i]
                urls_1.append(url_1)
            i = i + 1

    # 去重
    urls = list(set(urls))
    # 返回处理后的url列表
    return urls_1

# 后缀名仓库
suffixs = ('.001','.002','.1','.2','.7z','.arj','.back','.backup','.bak','.bakup','.bas','.bz2','.c','.cab','.conf','.copia',
'.core','.cpp','.dat','.db','.default','.dll','.doc','.gz','.ini',
'.jar','.java','.metalink','.old','.orig','.pas','.rar','.sav','.saved','.source','.src','.stackdump','.tar','.tar.gz',
'.tar.gz.metalink','.temp','.test','.tgz','.tmp','.txt','.war','.Z','.zip','.uue','.iso','.7-zip','.ace','.lzh','.gzip')


class RedisUN(threading.Thread):
    def __init__(self, queue1):
        threading.Thread.__init__(self)
        self._queue = queue1

    def run(self):
        while True:
            if self._queue.empty():
                break
            # 实际工作的代码区域
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
                    print('检测报错！')
                    continue


def main():
    global f2
    f2 = open('jieguo.txt', 'w+')  # 检测的结果存在这个文件夹里。

    xujiancedeURL = neirongtianjia_hou_txt('url.txt')  # burp导出的url列表放在这里

    thread_count = 100  # 线程数
    threads = []
    queue1 = queue.Queue()

    for line in xujiancedeURL:
        line = line.strip('\n').strip('\ufeff')   # 读取每一行
        queue1.put(line)

    for i in range(thread_count):
        threads.append(RedisUN(queue1))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    f2.close()


if __name__ == '__main__':
    main()
