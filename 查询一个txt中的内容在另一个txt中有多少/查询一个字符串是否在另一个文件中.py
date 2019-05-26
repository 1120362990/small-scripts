# -*- coding: utf-8 -*-


def str_search(target_txt, assets_txt):
    # 第一个参数危要查寻的txt，第二个为被查询的txt
    # 获取要查找的字符串
    targets = []
    f = open(target_txt, "r")
    lines = f.readlines()
    for line in lines:
        targets.append(line.strip())

    # 获取被查找的字符串
    assets = []
    f1 = open(assets_txt, "r")
    lines1 = f1.readlines()
    for line in lines1:
        assets.append(line.strip())

    for target in targets:
        if target in assets:
            pass
            # 输出两个txt共有的
            print(target)
        # else:
            # 输出不是两个txt共有的
            # print(target)


if __name__ == "__main__":
    str_search("target.txt", "assets.txt")
