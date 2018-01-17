import sys
#--coding='utf-8'--
i=1

while i <3:
    username=input("请输入用户名：")
    lock_file=open('user_lock.txt','r+')
    lock_list=lock_file.readlines()

    for lock_line in lock_list:
        lock_line=lock_line.strip('\n')
        if(username==lock_line):
            sys.exit("该账户%s已经冻结"%username)

    user_file=open('user_id.txt','r')
    user_list=user_file.readlines()
    for user_line in user_list:
        (user,password)=user_line.strip('\n').split()
        if username==user:
            m=0
            while m<3:
                passwd=input("请输入密码：")
                m+=1
                if passwd == password:
                    print("%s欢迎登陆~"%username)
                else:
                    if m!=3:
                        print("用户%s密码错误，还有%d次机会"%(username,3-m)

                    else:
                        lock_file.write(username+"\n")
                        sys.exit("%s用户达到最大登陆次数，请联系管理员！"%username)
        else:
            pass
    else:
        if i!=2:
            print("用户%s不存在，请重新输入，还有%d次机会！"%（username,2-i）)
    i+=1
else:
    sys.exit("用户%s不存在，退出"%username)

lock_file.close()
user_file.close()

