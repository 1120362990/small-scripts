#coding=utf-8
import fnmatch

#此函数匹配结果对大小写不敏感
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

#此函数对大小写敏感
def test(file):
    print(file)
    targets = ['UEMP_MSG_CDR_T','UEMP_CHANNEL_CDR_T','UEMP_CAS_CDR_T']
    wenben = open(file,encoding='gbk',errors='ignore')
    for hang in wenben:
        for target in targets:
            if target in hang:
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




