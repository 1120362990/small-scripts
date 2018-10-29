#coding=utf-8




def main(user,passwd):
    print(user,passwd)
    users = open("user.txt","r")
    passwds = open("passwd.txt","r")
    for user in users:
        for passwd in passwds:
            print(user.strip()+':'+passwd.strip())
            result.write(user.strip()+':'+passwd.strip()+'\n')
    users.close()
    passwds.close()


if __name__ == '__main__':
    result = open('result.txt','w+')
    main('user.txt','passwd.txt')
    result.close()