# -*- coding: utf-8 -*-
import math


def fj(path,number):
    fi = open(path)
    txt = fi.readlines()
    ips = []
    for w in txt:
        w = w.strip()
        ips.append(w.strip('\n'))
    print('all ips',len(ips))

    n = len(ips)/float(number)
    
    print('n',n)

    x = 0 -number
    y = number - 1 -number

    for n in range(math.ceil(n)):
        print(n)
        x = x + number
        y = y + number
        print(x)
        print(y)
        sss = len(ips)-x
        if sss>number-2:
            ips_1 = ips[x:y]
            for ip in ips_1:
                with open(path[:-4]+'-'+str(n)+'.txt', 'a') as out_file:
                    out_file.write(ip+'\n')
        else:
            ips_1 = ips[x:]
            for ip in ips_1:
                with open(path[:-4]+'-'+str(n)+'.txt', 'a') as out_file:
                    out_file.write(ip+'\n')



if __name__ == "__main__":
    fj(r'F:\100000086.txt',50000)





# def fj(path,number,outname):
#     fi = open(path)
#     txt = fi.readlines()
#     ips = []
#     for w in txt:
#         w = w.strip()
#         ips.append(w.strip('\n'))
#     print('all ips',len(ips))

#     n = len(ips)/float(number)
    
#     print('n',n)

#     x = 0 -number
#     y = number - 1 -number

#     for n in range(math.ceil(n)):
#         print(n)
#         x = x + number
#         y = y + number
#         print(x)
#         print(y)
#         sss = len(ips)-x
#         if sss>49998:
#             ips_1 = ips[x:y]
#             for ip in ips_1:
#                 with open(outname+'\domains_result'+str(n)+'.txt', 'a') as out_file:
#                     out_file.write(ip+'\n')
#         else:
#             ips_1 = ips[x:]
#             for ip in ips_1:
#                 with open(outname+'\domains_result'+str(n)+'.txt', 'a') as out_file:
#                     out_file.write(ip+'\n')



# if __name__ == "__main__":
#     pass
