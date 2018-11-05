#coding=utf-8
import fnmatch



# def main(wenjianming):
#     print(wenjianming)
#     wenben = open(wenjianming,"r")
#     for hang in wenben:
#         if fnmatch.fnmatch(hang,'*ssh*'):
#             print(hang)
#         elif fnmatch.fnmatch(hang,'*root*'):
#             print(hang)
#         elif fnmatch.fnmatch(hang,'*ping*'):
#             print(hang)
#         elif fnmatch.fnmatch(hang,'*telnet*'):
#             print(hang)
#         elif fnmatch.fnmatch(hang,'*select*'):
#             print(hang)
#         elif fnmatch.fnmatch(hang,'*where*'):
#             print(hang)
#         elif fnmatch.fnmatch(hang, '*AND*'):
#             print(hang)
#         elif fnmatch.fnmatch(hang, '*From*'):
#             print(hang)
#         else:
#             print(hang)
#             result.write(hang.strip()+'\n')
#     wenben.close()

def main(wenjianming):
    print(wenjianming)
    wenben = open(wenjianming,encoding='gbk',errors='ignore')
    for hang in wenben:
        if fnmatch.fnmatch(hang, '*UEMP_MSG_CDR_T*') or \
        fnmatch.fnmatch(hang, '*UEMP_CHANNEL_CDR_T*') or \
        fnmatch.fnmatch(hang, '*UEMP_CAS_CDR_T*'):
            try:
                print(hang)
                result2.write(hang.strip() + '\n')
            except:
                continue
        else:
            print(hang)
            result.write(hang.strip()+'\n')
    wenben.close()



if __name__ == '__main__':
    result = open('sss_1.csv','w+')
    result2 = open('sss_2.csv', 'w+')
    main('sss.csv')
    result.close()
    result2.close()
    print('ok')




