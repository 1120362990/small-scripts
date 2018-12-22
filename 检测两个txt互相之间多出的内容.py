# -*- coding: utf-8 -*-
import xlwt
def test(name1,name2):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, name1)
    worksheet.write(0, 1, name2)
    worksheet.write(0, 2, name1+'多出')
    worksheet.write(0, 3, name2+'多出')
    a, b, c, d = 1, 1, 1, 1
    txt1 = open(name1,"r")
    txt2 = open(name2,"r")
    list1 = []
    list2 = []
    for txt in txt1:
        list1.append(txt.strip())
        worksheet.write(a, 0, txt.strip())
        a = a + 1
    for txt in txt2:
        list2.append(txt.strip())
        worksheet.write(b, 1, txt.strip())
        b = b + 1
    print('开始检测'+name1)
    for list in list1:
        if list in list2:
            print(str(list)+'存在')
        else:
            print(str(list) + '不存在')
            worksheet.write(c, 2, str(list))
            c = c + 1
    print('开始检测'+name2)
    for list in list2:
        if list in list1:
            print(str(list)+'存在')
        else:
            print(str(list) + '不存在')
            worksheet.write(d, 3, str(list))
            d = d + 1
    workbook.save('jieguo.xls')
    print('文件创建完成')

if __name__ == "__main__":
    test('1.txt','2.txt') #两个txt作为输入，分别存放要对比的内容