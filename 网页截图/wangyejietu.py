# -*- coding: utf-8 -*-
import requests
import time
import os
from selenium import webdriver

 
'''
def jietu(domain,num):
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome()#开启浏览器
    browser.set_window_size(1300, 1200)#控制浏览器大小的玩意
    browser.set_page_load_timeout(2)  #设置超时时间
    browser.get("http://%s/" % domain)#请求网页
    #time.sleep(2)#延时
    browser.save_screenshot("%s.png" % num)#截屏
    browser.quit()#浏览器关闭
'''

#这个加了请求超时，稳定性有待测试。接下来加上进度情况。看结果http和https有没有影响
def jietu(domain,num):
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome()#开启浏览器
    browser.set_window_size(1300, 1200)#控制浏览器大小的玩意

    browser.set_page_load_timeout(30)
    browser.maximize_window()
    try:
        #browser.get("http://%s/" % domain)#请求网页
        browser.get(domain)#请求网页
        browser.save_screenshot("%s.png" % num)#截屏
        browser.quit()#浏览器关闭
    except:
        print('load timeout')
        browser.quit()#浏览器关闭




if __name__ == "__main__":
    global X 
    X = 0
    outfile = open('jieguo.txt', 'w')
    for domain in open('domains.txt'):
        jietu(domain,X)
        outfile.write(domain.strip()+'  '+str(X)+'\n')
        X = X + 1
    outfile.close()
    try:
        os.remove('geckodriver.log')
    except:
        print(' ')




