#coding=utf-8
import sys
key = sys.argv[1]
f = open("%s.txt"%key,"a")
list1 = [123,321,1234,4321,123456,654321,12345678,123456789,1234567890,888,8888,666,6666,163,521,1314,1,11,111,1111,2,222,3,333,5,555,9,999]
list2 = ['#123','#1234','#123456','@123','@1234','@123456','@qq.com','qq.com','@123.com','123.com','@163.com','163.com','126.com','!@#','!@#$','!@#$%^','098']
for j1 in list1:
    pwd1 =  key + str(j1) + '\n'
    f.write(pwd1)
for j2 in list2:
    pwd2 =  key+str(j2)+'\n'
    f.write(pwd2)

for i in range(1980,2016):
    #pwd1 = key + str(i) + '\n'
    pwd3 = '{}{}{}'.format(key,i,'\n')
    f.write(pwd3)


f.close()
print(key+' password combination ok!!!')