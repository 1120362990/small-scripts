# -*- coding:utf-8 -*-

# userage ： 将此文件与需要合并的txt放到一个目录下，双击即可

import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # 获取当前路径下所有非目录子文件，去掉本python文件的名字
        files.remove('合并多个txt.py')
        return files


# 合并结果
def merge(files):
    for file in files:
        print(file)
        with open(file, 'r', encoding = 'utf-8') as f:
            for line in f:
                data = f.read()  # 读取文件
                # print(data)
                with open('merge_result.txt', 'a') as out_file:
                    out_file.write(data)


# 活动当前工作目录路径
file_dir = os.getcwd()
os.chdir(file_dir)


# 删除可能已存在的结果同名文件
try:
    os.remove('merge_result.txt')
except Exception:
    pass

# 获取到所有文件名，已去掉python文件本身
files = file_name(file_dir)

print(files)
merge(files)
