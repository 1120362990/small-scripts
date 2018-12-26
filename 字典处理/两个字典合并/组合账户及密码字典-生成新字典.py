#coding=utf-8




def main(user,passwd):
    users = open("user.txt","r")
    for user in users:
        passwds = open("passwd.txt", "r")
        for passwd in passwds:
            print(user.strip()+':'+passwd.strip())
            result.write(user.strip()+passwd.strip()+'\n')


if __name__ == '__main__':
    result = open('result.txt','w+')
    main('user.txt','passwd.txt')
    result.close()