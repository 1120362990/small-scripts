# -*- coding: utf-8 -*-
import zipfile
import os
import shutil
import xlrd
from xlrd import xldate_as_tuple
import csv


# 压缩包解压缩，删除无用文件
def compress(zip_path):
    # 获得压缩包的文件路径，文件就解压到这个路径下
    file_path = zip_path[:zip_path.rfind('\\')]

    # 解压缩文件
    zipfile.ZipFile(zip_path).extractall(file_path+'\\file_tem125632')

    #删除不必要文件
    os.remove(file_path+'\\file_tem125632\\index.xls')
    shutil.rmtree(file_path+'\\file_tem125632\\vulnhostsfiles')

    # 返回解压后的文件路径
    return file_path+'\\file_tem125632'


#获取指定文件夹下的文件名称++++++++++++++++++++++++++++++++++++++
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        try:
            files.remove('desktop.ini')
        except:
            pass
        return(files)

#读取xls文件,返回IP漏洞数据列表
# read_xls(r'F:\OneDrive\工作\辽宁移动铁岭地市\铁岭移动漏洞统计脚本\file_tem125632\\','221.180.150.40.xls')
def read_xls(xls_path,xls_name):
    inf_dict = []
    # 处理xls文件路径，判断xls_path最后有没有/
    if xls_path[-1] != '\\':
        xls_path = xls_path + '\\'
    else:
        pass
    workbook = xlrd.open_workbook(xls_path+xls_name,"r")    #打开excel文件
    sheet = workbook.sheet_by_name(r'漏洞信息')
    i = 1
    while i < sheet.nrows:
        if (sheet.cell(i,0).value == ''):
            IP地址=xls_name[0:-4]
            try:
                端口= int(duankou)
            except Exception:
                端口= duankou
            协议= xieyi
            服务= fuwu
            漏洞名称= sheet.cell(i,3).value
            漏洞风险值= int(sheet.cell(i,4).value)
            风险等级= sheet.cell(i,5).value
            服务分类= sheet.cell(i,6).value
            应用分类= sheet.cell(i,7).value
            系统分类= sheet.cell(i,8).value
            威胁分类= sheet.cell(i,9).value
            时间分类= sheet.cell(i,10).value
            CVE年份分类= sheet.cell(i,11).value
            发现日期= str(xldate_as_tuple(sheet.cell(i,12).value,0)[0])+'-'+str(xldate_as_tuple(sheet.cell(i,12).value,0)[1])+'-'+str(xldate_as_tuple(sheet.cell(i,12).value,0)[2])
            CVE编号= sheet.cell(i,13).value
            CNNVD编号= sheet.cell(i,14).value
            CNCVE编号= sheet.cell(i,15).value
            CNVD编号= sheet.cell(i,16).value
            详细描述= sheet.cell(i,17).value
            解决办法= sheet.cell(i,18).value
            返回信息= sheet.cell(i,19).value
            inf_dict.append([IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,服务分类,应用分类,系统分类,威胁分类,时间分类,CVE年份分类,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息])
            i = i + 1
        else:
            IP地址=xls_name[0:-4]
            try:
                端口= int(sheet.cell(i,0).value)
            except Exception:
                端口= sheet.cell(i,0).value
            协议= sheet.cell(i,1).value
            服务= sheet.cell(i,2).value
            漏洞名称= sheet.cell(i,3).value
            漏洞风险值= int(sheet.cell(i,4).value)
            风险等级= sheet.cell(i,5).value
            服务分类= sheet.cell(i,6).value
            应用分类= sheet.cell(i,7).value
            系统分类= sheet.cell(i,8).value
            威胁分类= sheet.cell(i,9).value
            时间分类= sheet.cell(i,10).value
            CVE年份分类= sheet.cell(i,11).value
            发现日期= str(xldate_as_tuple(sheet.cell(i,12).value,0)[0])+'-'+str(xldate_as_tuple(sheet.cell(i,12).value,0)[1])+'-'+str(xldate_as_tuple(sheet.cell(i,12).value,0)[2])
            CVE编号= sheet.cell(i,13).value
            CNNVD编号= sheet.cell(i,14).value
            CNCVE编号= sheet.cell(i,15).value
            CNVD编号= sheet.cell(i,16).value
            详细描述= sheet.cell(i,17).value
            解决办法= sheet.cell(i,18).value
            返回信息= sheet.cell(i,19).value
            duankou = 端口
            xieyi = 协议
            fuwu = 服务
            inf_dict.append([IP地址,端口,协议,服务,漏洞名称,漏洞风险值,风险等级,服务分类,应用分类,系统分类,威胁分类,时间分类,CVE年份分类,发现日期,CVE编号,CNNVD编号,CNCVE编号,CNVD编号,详细描述,解决办法,返回信息])
            i = i + 1
    return inf_dict

def main(zip_path):
    path = compress(zip_path)
    print(path)
    inf_dicts = []
    for xls in file_name(path):
        inf_dicts= inf_dicts + read_xls(path,xls)

    headers = ['IP地址','端口','协议','服务','漏洞名称','漏洞风险值','风险等级','服务分类','应用分类','系统分类','威胁分类','时间分类','CVE年份分类','发现日期','CVE编号','CNNVD编号','CNCVE编号','CNVD编号','详细描述','解决办法','返回信息']

    with open(zip_path[:zip_path.rfind('\\')+1]+zip_path[zip_path.rfind('\\')+1:-4]+'.csv','a+',newline='',encoding = 'utf-8')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(inf_dicts)
    shutil.rmtree(path)


if __name__ == "__main__":
    main(r"F:\\2020_04_10_xls.zip")
