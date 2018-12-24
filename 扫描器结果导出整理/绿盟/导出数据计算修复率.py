# -*- coding: utf-8 -*-

import xlwt
import xlrd

class Xls:
    def __init__(self):
        self.name = None
        self.workbook = None
        self.sheet = None
    #设置xls_name和sheet_name
    def initialization(self,xls_name,sheet_name):
        self.name = xls_name + '.xls'
        self.workbook = xlrd.open_workbook(self.name)
        self.sheet = self.workbook.sheet_by_name(sheet_name)
    #获取行数
    def nrow_xls(self):
        return self.sheet.nrows
    #获取单元格中的值
    def get_valu(self,x,y):
        return self.sheet.cell(y,x).value

if __name__ == "__main__":
    #类、实例化
    xls = Xls()
    #初始化
    xls.initialization('月度漏洞库-181023-公网及内网漏洞新发现情况统计',u'各系统本月漏洞现状')
    #获取某个单元格中的值
    #print(xls.get_valu(0,0))
    #获取行数
    #print(xls.nrow_xls())

    # l 高危共发现 已修复 未修复 中危共发现 已修复 未修复 问题IP数量
    #共发现漏洞数量 已修复漏洞数量 未修复漏洞数量 修复率 问题IP数量
    l = [
        ['公网',0,0,0,0,0,0,0],
        ['内网',0,0,0,0,0,0,0],
        ['无归属',0,0,0,0,0,0,0],
        ['公网',0,0,0,0,0],
        ['内网',0,0,0,0,0]
    ]

    for y in range(3,xls.nrow_xls()):
        #print(x)
        f = xls.get_valu(3,y)
        if f =='公网':
            l[0][1]=l[0][1]+int(xls.get_valu(4,y))
            l[0][2] = l[0][2] + int(xls.get_valu(5, y))
            l[0][3] = l[0][3] + int(xls.get_valu(6, y))
            l[0][4] = l[0][4] + int(xls.get_valu(7, y))
            l[0][5] = l[0][5] + int(xls.get_valu(8, y))
            l[0][6] = l[0][6] + int(xls.get_valu(9, y))
            l[0][7] = l[0][7] + int(xls.get_valu(10, y))
        elif f =='内网':
            l[1][1] = l[1][1] + int(xls.get_valu(4, y))
            l[1][2] = l[1][2] + int(xls.get_valu(5, y))
            l[1][3] = l[1][3] + int(xls.get_valu(6, y))
            l[1][4] = l[1][4] + int(xls.get_valu(7, y))
            l[1][5] = l[1][5] + int(xls.get_valu(8, y))
            l[1][6] = l[1][6] + int(xls.get_valu(9, y))
            l[1][7] = l[1][7] + int(xls.get_valu(10, y))
        else:
            l[2][1] = l[2][1] + int(xls.get_valu(4, y))
            l[2][2] = l[2][2] + int(xls.get_valu(5, y))
            l[2][3] = l[2][3] + int(xls.get_valu(6, y))
            l[2][4] = l[2][4] + int(xls.get_valu(7, y))
            l[2][5] = l[2][5] + int(xls.get_valu(8, y))
            l[2][6] = l[2][6] + int(xls.get_valu(9, y))
            l[2][7] = l[2][7] + int(xls.get_valu(10, y))

    l[3][1]=l[0][1]+l[0][4]
    l[3][2] =l[0][2]+l[0][5]
    l[3][3] =l[0][3]+l[0][6]
    l[3][4] = '{:.0%}'.format(l[3][2]/l[3][1])
    l[3][5] =l[0][7]

    l[4][1] = l[1][1] + l[1][4]
    l[4][2] = l[1][2] + l[1][5]
    l[4][3] = l[1][3] + l[1][6]
    l[4][4] = '{:.0%}'.format(l[4][2] / l[4][1])
    l[4][5] = l[1][7]

    for ll in l:
        print(ll)
