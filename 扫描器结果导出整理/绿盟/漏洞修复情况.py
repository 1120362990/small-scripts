# -*- coding: utf-8 -*-
import sqlite3

#现在的功能，可以向旧表中写入已修复的漏洞和未修复的漏洞
def mainjiubiaochuli(Main_DB,oldtable,newtable):#三个参数依次是： 数据库  旧的漏洞统计表  新的漏洞统计表
    conn = sqlite3.connect(Main_DB)#建立数据库连接
    cursor = conn.cursor()
    oldtable_biao = '\''+oldtable+'\''  #旧表连接
    newtable_biao = '\''+newtable+'\''  #新表连接

    cursor.execute("SELECT ID FROM %s" % oldtable_biao)#从旧表中提取ID列，作为遍历的基准数据
    a = cursor.fetchall()#获取所有的ID

    number = 0
    while number < len(a):
        print("ID:"+str(a[number][0])+"  Now:"+str(number+1)+"  Total:"+str(len(a)))#打印正在处理的漏洞ID，现在已经处理了多少个漏洞，一共需要查询的漏洞总数
        cursor.execute("SELECT * FROM %s WHERE ID = %s" % (oldtable_biao,a[number][0]))#获取旧表中ID对应的漏洞
        b = cursor.fetchall()
        #print(b)#获取存在漏洞的系统的信息
        print(b[0][5])#获取漏洞IP
        print(b[0][6])#获取漏洞端口
        print(b[0][9])#获取漏洞名称
        cursor.execute('SELECT * FROM '+newtable_biao+' WHERE IP地址 = ? AND 端口 = ? AND 漏洞名称 = ?' , (b[0][5],b[0][6],b[0][9]))
        #依次在新表中查询旧表中存在的漏洞，可能出现两种情况，第一是新标中没发现此漏洞，返回值长度为0。另一种是仍发现了这个漏洞，返回一条数据，返回值为1
        c = cursor.fetchall()
        print(len(c))#获取存在漏洞的系统的信息
        if len(c) == 1:
            print("本次扫描再次发现该漏洞，以上漏洞未修复")
            cursor.execute("UPDATE %s SET 修复情况 = '未修复' WHERE ID ='%s'" % (oldtable_biao,a[number][0]))
            conn.commit()
        else:
            print("本次扫描未发现该漏洞，此漏洞应已修复。")
            #cursor.execute("UPDATE %s SET 修复情况 = '已修复' WHERE ID ='%s'" % (oldtable_biao,number))
            cursor.execute("UPDATE %s SET 修复情况 = '已修复' WHERE ID ='%s'" % (oldtable_biao, a[number][0]))
            conn.commit()
        print("------------------")
        number = number + 1
    conn.close()

def mainxinbiaochuli(Main_DB,oldtable,newtable):#三个参数依次是： 数据库  旧的漏洞统计表  新的漏洞统计表
    conn = sqlite3.connect(Main_DB)#建立数据库连接
    cursor = conn.cursor()
    oldtable_biao = '\''+oldtable+'\''  #旧表连接
    newtable_biao = '\''+newtable+'\''  #新表连接

    cursor.execute("SELECT ID FROM %s" % newtable_biao)#从新表中提取ID列，作为遍历的基准数据
    a = cursor.fetchall()#获取所有的ID

    number = 0
    while number < len(a):
        print("ID:"+str(a[number][0])+"  Now:"+str(number+1)+"  Total:"+str(len(a)))#打印正在处理的漏洞ID，现在已经处理了多少个漏洞，一共需要查询的漏洞总数
        cursor.execute("SELECT * FROM %s WHERE ID = %s" % (newtable_biao,a[number][0]))#获取新表中ID对应的漏洞
        b = cursor.fetchall()
        #print(b)#获取存在漏洞的系统的信息
        print(b[0][5])#获取漏洞IP
        print(b[0][6])#获取漏洞端口
        print(b[0][9])#获取漏洞名称
        cursor.execute('SELECT * FROM '+oldtable_biao+' WHERE IP地址 = ? AND 端口 = ? AND 漏洞名称 = ?' , (b[0][5],b[0][6],b[0][9]))
        #依次在旧表中查询新表中存在的漏洞，可能出现两种情况，第一是旧标中没发现此漏洞，返回值长度为0。另一种是仍发现了这个漏洞，返回一条数据，返回值为1
        c = cursor.fetchall()
        print(len(c))#获取存在漏洞的系统的信息
        if len(c) == 1:
            print("上次扫描已发现该漏洞，此漏洞未修复")
            cursor.execute("UPDATE %s SET 修复情况 = '未修复' WHERE ID ='%s'" % (newtable_biao,a[number][0]))
            conn.commit()
        else:
            print("上次扫描未发现该漏洞，此漏洞为新发现。")
            #cursor.execute("UPDATE %s SET 修复情况 = '已修复' WHERE ID ='%s'" % (newtable_biao,number))
            cursor.execute("UPDATE %s SET 修复情况 = '新发现' WHERE ID ='%s'" % (newtable_biao, a[number][0]))
            conn.commit()
        print("------------------")
        number = number + 1
    conn.close()

def wubaochuli(Main_DB,wubaoloudong,newtable):#三个参数依次是： 数据库  误报漏洞统计表  漏洞修复状态统计表
    conn = sqlite3.connect(Main_DB)#建立数据库连接
    cursor = conn.cursor()
    wubaotable_biao = '\''+wubaoloudong+'\''  #误报漏洞表连接
    newtable_biao = '\''+newtable+'\''  #漏洞修复状态统计表连接

    cursor.execute("SELECT ID FROM %s" % wubaotable_biao)#从误报漏洞表中提取ID列，作为遍历的基准数据
    a = cursor.fetchall()#获取所有的ID

    number = 0
    while number < len(a):
        print("ID:"+str(a[number][0])+"  Now:"+str(number+1)+"  Total:"+str(len(a)))#打印正在处理的漏洞ID，现在已经处理了多少个漏洞，一共需要查询的漏洞总数
        cursor.execute("SELECT * FROM %s WHERE ID = %s" % (wubaotable_biao,a[number][0]))#获误报漏洞表中ID对应的漏洞
        b = cursor.fetchall()
        #print(b)#获取存在漏洞的系统的信息
        print(b[0][5])#获取漏洞IP
        print(b[0][6])#获取漏洞端口
        print(b[0][9])#获取漏洞名称
        cursor.execute('SELECT * FROM '+newtable_biao+' WHERE IP地址 = ? AND 端口 = ? AND 漏洞名称 = ?' , (b[0][5],b[0][6],b[0][9]))
        #依次在新表中查询误报漏洞表中存在的漏洞，可能出现两种情况，第一是新标中没发现此漏洞，返回值长度为0。另一种是仍发现了这个漏洞，返回一条数据，返回值为1
        c = cursor.fetchall()
        print(len(c))#获取的系统的信息
        if len(c) == 1:
            print("发现误报漏洞。")
            cursor.execute("UPDATE %s SET 修复情况 = '误报' WHERE ID ='%s'" % (newtable_biao,c[0][0]))
            conn.commit()
        else:
            print("未发现该误报漏洞。")
        print("------------------")
        number = number + 1
    conn.close()

if __name__ == "__main__":
    #mainjiubiaochuli('E:\\python\\归属查询\\hulianwang.db',"月度漏洞库-181129-公网及内网","月度漏洞库-181229-公网及内网")#三个参数依次是： 数据库  旧的漏洞统计表  新的漏洞统计表
    #mainxinbiaochuli('E:\\python\\归属查询\\hulianwang.db',"月度漏洞库-181129-公网及内网","月度漏洞库-181229-公网及内网")#三个参数依次是： 数据库  旧的漏洞统计表  新的漏洞统计表
    wubaochuli('E:\\python\\归属查询\\hulianwang.db','互联网中心误报漏洞库-181224','周常漏洞库-190107-公网及内网') #三个参数依次是： 数据库  误报漏洞统计表  漏洞修复状态统计表



