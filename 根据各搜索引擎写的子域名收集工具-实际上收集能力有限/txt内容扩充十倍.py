# -*- coding: utf-8 -*-
lines = open("foo.txt")
fw = open("jiguo.txt","w")
for line in lines:
    print line
    i = 0
    while i < 10:
        fw.write(line.strip()+'\n')
        i = i + 1
        print i   
fw.close()
lines.close()
