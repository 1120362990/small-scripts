from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
from tkinter import ttk
import requests
import time
import urllib3
import threading


class MainPage(object):
    def __init__(self, master=None):
        self.root = master #定义内部变量root
        self.root.geometry('%dx%d' % (900, 680)) #设置窗口大小
        self.createPage()

    def createPage(self):
        self.findbak_dan_page = FindbakFrame(self.root) # 创建不同Frame
        self.findbak_dan_page.pack() #默认显示数据录入界面
        menubar = Menu(self.root)
        menubar.add_command(label='压缩文件检测', command = self.findbak_dan)
        self.root['menu'] = menubar  # 设置菜单栏

    def findbak_dan(self):
        self.findbak_dan_page.pack()

class FindbakFrame(Frame): # 继承Frame类
    #声明，不用动
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master #定义内部变量root
        self.url = StringVar()
        self.createPage()

    def createPage(self):
        #找备份文件的函数
        def zhaobeifenweijian_duomulu():
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            jcgc.insert('1.0', '开始检测。' + "\n")
            def findbak_ciji_catlog_urls(urlsx):
                suffixs = (
                    '.001', '.002', '.1', '.2', '.7z', '.arj', '.back', '.backup', '.bak',
                    '.bakup', '.bas', '.bz2', '.c', '.cab', '.conf', '.copia', '.core', '.cpp',
                    '.dat', '.db', '.default', '.dll', '.doc', '.gz', '.ini', '.jar', '.java',
                    '.metalink', '.old', '.orig', '.pas', '.rar', '.sav', '.saved', '.source',
                    '.src', '.stackdump', '.tar', '.tar.gz', '.tar.gz.metalink', '.temp',
                    '.test', '.tgz', '.tmp', '.txt', '.war', '.Z', '.zip')
                for urls in urlsx:
                    for suffix in suffixs:
                        url = urls + suffix
                        try:
                            r = requests.get(url, verify=False, allow_redirects=False)
                            jcgc.insert('1.0', 'Content-Length:' + r.headers.get('Content-Length') + '   ' + str(
                                r.status_code) + '    ' + url + '\n')
                            self.update_idletasks()  # 实时刷新
                            if str(r.status_code) == str(200):
                                wenti.insert('1.0', 'Content-Length:' + r.headers.get(
                                    'Content-Length') + '   ' + '可能存在问题    ' + url + '\n')
                                self.update_idletasks()  # 实时刷新
                        except Exception:
                            jcgc.insert('1.0', 'Content-Length:' + str(
                                r.headers.get('Content-Length')) + '   ' + 'someerror    ' + url + '\n')
                            self.update_idletasks()  # 实时刷新

            # 处理所提供发的url，处理后为主目录及所有二级目录的形式
            def url_handle(url):
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

            # 根据域名生成主目录爆破文件名，并进行爆破
            def findbak_zhu_catlog(url_f):
                url = url_f
                suffixList = ['.rar', '.zip', '.sql', '.gz', '.tar', '.bz2', '.tar.gz', '.bak', '.dat']
                keyList = ['install', 'INSTALL', 'index', 'INDEX', 'ezweb', 'EZWEB', 'flashfxp', 'FLASHFXP', '111', '1','upload']
                if (url[:5] == 'http:'):
                    url = url[7:].strip()
                if (url[:6] == 'https:'):
                    url = url[8:].strip()
                numT = url.find('/')
                if (numT != -1):
                    url = url - url[:numT]
                # 根据URL，推测一些针对性的文件名:
                num1 = url.find('.')
                num2 = url.find('.', num1 + 1)
                keyList.append(url[num1 + 1:num2])
                keyList.append(url[num1 + 1:num2].upper())
                keyList.append(url)  # www.test.com
                keyList.append(url.upper())
                keyList.append(url.replace('.', '_'))  # www_test_com
                keyList.append(url.replace('.', '_').upper())
                keyList.append(url.replace('.', ''))  # wwwtestcom
                keyList.append(url.replace('.', '').upper())
                keyList.append(url[num1 + 1:])  # test.com
                keyList.append(url[num1 + 1:].upper())
                keyList.append(url[num1 + 1:].replace('.', '_'))  # test_com
                keyList.append(url[num1 + 1:].replace('.', '_').upper())
                tempList = []
                for key in keyList:
                    for suff in suffixList:
                        tempList.append(key + suff)
                for temp in tempList:
                    url = url_f + '/' + temp
                    try:
                        r = requests.get(url, verify=False, allow_redirects=False)
                        jcgc.insert('1.0', 'Content-Length:' + r.headers.get('Content-Length') + '   ' + str(
                            r.status_code) + '    ' + url + '\n')
                        self.update_idletasks()  # 实时刷新
                        if str(r.status_code) == str(200):
                            wenti.insert('1.0', 'Content-Length:' + r.headers.get(
                                'Content-Length') + '   ' + '可能存在问题    ' + url + '\n')
                            self.update_idletasks()  # 实时刷新
                    except:
                        jcgc.insert('1.0', 'Content-Length:' + str(
                            r.headers.get('Content-Length')) + '   ' + 'someerror    ' + url + '\n')
                        self.update_idletasks()  # 实时刷新
            url = enter.get()
            findbak_zhu_catlog(url_handle(url)[0][:-1])  # 主目录备份文件爆破
            findbak_ciji_catlog_urls(url_handle(url)[1:])  # 次级目录备份扫描
            jcgc.insert('1.0', '检测完成。' + "\n")

        def zhaobeifenweijian_url():
            jcgc.insert('1.0', '开始检测。' + "\n")
            suffixs = (
                '.001', '.002', '.1', '.2', '.7z', '.arj', '.back', '.backup', '.bak',
                '.bakup', '.bas', '.bz2', '.c', '.cab', '.conf', '.copia', '.core', '.cpp',
                '.dat', '.db', '.default', '.dll', '.doc', '.gz', '.ini', '.jar', '.java',
                '.metalink', '.old', '.orig', '.pas', '.rar', '.sav', '.saved', '.source',
                '.src', '.stackdump', '.tar', '.tar.gz', '.tar.gz.metalink', '.temp',
                '.test', '.tgz', '.tmp', '.txt', '.war', '.Z', '.zip')
            for suffix in suffixs:
                url = enter.get() + suffix
                # print(url)
                try:
                    r = requests.get(url, verify=False, allow_redirects=False)
                    jcgc.insert('1.0', 'Content-Length:' + r.headers.get('Content-Length') + '   ' + str(
                        r.status_code) + '    ' + url + '\n')
                    self.update_idletasks()  # 实时刷新
                    if str(r.status_code) == str(200):
                        wenti.insert('1.0', 'Content-Length:' + r.headers.get(
                            'Content-Length') + '   ' + '可能存在问题    ' + url + '\n')
                        self.update_idletasks()  # 实时刷新
                except:
                    jcgc.insert('1.0', 'Content-Length:' + str(
                        r.headers.get('Content-Length')) + '   ' + 'someerror    ' + url + '\n')
                    self.update_idletasks()  # 实时刷新
            jcgc.insert('1.0', '检测完成。' + "\n")

        Label(self,text = '压缩文件检测',font=("Arial", 20)).grid(row=0, stick=N, pady=10,columnspan=3)
        Label(self, text = '多级目录备份文件测试:').grid(row=1, column=0, stick=W, pady=10)
        Label(self, text='单级目录备份文件测试:').grid(row=3, column=0, stick=W, pady=10)

        var=StringVar()
        enter = Entry(self, textvariable = var,width=100)
        enter.grid(row=1, column=1, stick=E)#巨坑，grid显示哪个东西是很重要的
        enter = Entry(self, textvariable = var,width=100)
        enter.grid(row=3, column=1, stick=E)#巨坑，grid显示哪个东西是很重要的
        Button(self, text='检测', command = lambda:MyThread(zhaobeifenweijian_duomulu)).grid(row=1, column=2, stick=E, pady=10)
        Button(self, text='检测', command = lambda:MyThread(zhaobeifenweijian_url)).grid(row=3, column=2, stick=E, pady=10)
        Label(self, text = '检测过程:').grid(row=4, column=0, stick=W, pady=10)

        #设置带滑块的文本域:检测过程
        jcgc = Text(self,width=120,height=15)#设置文本框
        scrl_jcgc = Scrollbar(self)#设置下拉条
        scrl_jcgc.grid(row=5, column=4, stick=N+S)#下拉条位置
        jcgc.configure(yscrollcommand = scrl_jcgc.set)#不超过一屏不出现滑块
        jcgc.grid(row=5, columnspan=3, stick=N+S)#文本框位置
        scrl_jcgc['command'] = jcgc.yview#控制，拉动滚动条是内容开始滚动

        Label(self, text = '可能存在问题的项目:').grid(row=6, column=0, stick=W, pady=10)
        #设置带滑块的文本域:可能存在的问题
        wenti = Text(self,width=120,height=15)#设置文本框
        scrl_wenti = Scrollbar(self)#设置下拉条
        scrl_wenti.grid(row=7, column=4, stick=N+S)#下拉条位置
        wenti.configure(yscrollcommand = scrl_wenti.set)#不超过一屏不出现滑块
        wenti.grid(row=7, columnspan=3, stick=N+S)#文本框位置
        scrl_wenti['command'] = wenti.yview#控制，拉动滚动条是内容开始滚动

class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()
        self.func = func
        self.args = args
        self.setDaemon(True)
        self.start()    # 在这里开始
    def run(self):
        self.func(*self.args)


root = Tk()
root.title('压缩文件检测 by rpkr')
MainPage(root)
root.mainloop()
