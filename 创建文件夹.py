# -*- coding: utf-8 -*-
import os


names =(
'1',
'2',
'3'
)


for name in names:
    os.system("mkdir %s" % name)



print(os.system("dir"))