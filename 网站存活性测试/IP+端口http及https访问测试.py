# -*- coding: utf-8 -*-
import threading,queue
import requests
import xlwt
import urllib3


# 移除报错
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'


class LiveTest(threading.Thread):
    def __init__(self,queue1):
        threading.Thread.__init__(self)
        self._queue = queue1

    def run(self):
        while True:
            if self._queue.empty():
                break
            # 实际工作的代码区域
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', 'Connection': 'close'}
            url = self._queue.get(timeout=0.5)
            if url[:4] == 'http':
                try:
                    response = requests.get(url, headers=headers, timeout=60, verify=False).status_code
                    if response == 400:
                        try:
                            url1 = 'https://'+url
                            response = requests.get(url1, headers=headers, timeout=60, verify=False).status_code
                            self.OutPut(url1, str(response))
                            continue
                        except Exception as e:
                            self.OutPut(url, f'Error2: {str(e)}')
                            continue
                    else:
                        self.OutPut(url, str(response))
                    continue
                except Exception as e:
                    self.OutPut(url, f'Error1: {str(e)}')
                    continue
            else:
                try:
                    url1 = 'http://'+url
                    response = requests.get(url1, headers=headers, timeout=60, verify=False).status_code
                    if response == 400:
                        try:
                            url1 = 'https://'+url
                            response = requests.get(url1, headers=headers, timeout=60, verify=False).status_code
                            self.OutPut(url1, str(response))
                            continue
                        except Exception as e:
                            self.OutPut(url, f'Error2: {str(e)}')
                            continue
                    else:
                        self.OutPut(url1, str(response))
                    continue
                except requests.exceptions.ConnectionError:
                    try:
                        url2 = 'https://'+url
                        response = requests.get(url2, headers=headers, timeout=60, verify=False).status_code
                        self.OutPut(url2, str(response))
                        continue
                    except Exception as e:
                        self.OutPut(url, f'Error2: {str(e)}')
                        continue
                except Exception as e:
                    self.OutPut(url, f'Error3: {str(e)}')
                    continue

    def OutPut(self, url, stat):
        lock.acquire()
        print(url, '	', stat)
        Url_stat.append([url, stat])
        lock.release()


def main(filepath):
    global lock, worksheet, Url_stat
    Url_stat =[]#用来存放访问结果，最后存入xls
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('UrlStat')
    worksheet.write(0, 0, label='Url')
    worksheet.write(0, 1, label='Stat')
    xujiancedeURL = open(filepath, "r")  # 读取所要检测的url列表。就是提供给核心代码区域的参数
    thread_count = 1000  # 线程数
    threads = []
    queue1 = queue.Queue()
    lock = threading.Lock()
    for line in xujiancedeURL:
        line = line.strip()  # 读取每一行
        queue1.put(line)
    for i in range(thread_count):
        threads.append(LiveTest(queue1))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    xujiancedeURL.close()
    # 向xls文件中写如结果
    for x in range(1, len(Url_stat)+1):
        worksheet.write(x, 0, label=Url_stat[x-1][0])
        worksheet.write(x, 1, label=Url_stat[x-1][1])
    workbook.save('Result.xls')



if __name__ == '__main__':
    main(r"F:\URL.txt")
