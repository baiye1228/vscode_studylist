import os

user_path=r'F:\vscode\code_list\study_list\小案例\图书管理demo_by\用户资料_by\user.txt'
books_path=r'F:\vscode\code_list\study_list\小案例\图书管理demo_by\图书资料_by'

#用户注册
def register():
    print('*'*40)
    print('新用户注册')
    print('*'*40)
    while True:
        username=input('\t输入用户名：')
        password=input('\t输入密码：')
        repassword=input('\t确认密码：')
        with open(user_path,'r') as rstream:
            check=rstream.read()
            if username in check:
                print('用户名已存在！请重新输入！')
                continue
        if password==repassword:
            with open(user_path,'a') as wstream:
                wstream.write('{}  {}\n'.format(username,password))
                print('------------恭喜您注册成功！-------------')
                break
        else:
            print('密码不一致！请重新输入！')


#register()

#用户登录
def login():
    global islogin
    print('*'*40)
    print('用户登录')
    print('*'*40)
    while True:
        username=input('\t输入用户名：')
        password=input('\t输入密码：')
        def check():
            if username and password:
                with open(user_path) as rstream:
                    while True:
                        user=rstream.readline()
                        if not user:
                            print('用户名或密码错误！请重新输入！')
                            return 0
                        user_input='{}  {}\n'.format(username,password)
                        if user==user_input:
                            print('----------恭喜你登陆成功----------')
                            return 1
        if check()==1:
            islogin=True
            break

#login()

islogin=False  #判断登录状态

def books():
    print('*'*40)
    print('\t书架')
    print('*'*40)
    while True:
        choice=int(input('\t1.查看书本\n\t2.删除书本\n\t3.添加书本\n\t4.增加新目录\n\t5.退出选择\n请选择：'))
        if choice==1:
            
                books_list=os.listdir(books_path)
                for book in books_list:
                    book=book.replace('.txt','')
                    print('\t',book)
                
        elif choice==2:
            while True:
                delete=input('请输入您需要删除的书：')
                name=delete+'.txt'
                if name in books_list:
                    os.remove(os.path.join(books_path,name))
                    print('删除成功！')
                    break
                else:
                    print('输入错误或无此书！')

        elif choice==3:
            create=input('输入你需要添加的书：')
            file=open(books_path+create+'.txt','w')
            file.close()

        elif choice==4:
            credir=input('输入你需要添加的目录：')
            os.mkdir(books_path+credir)

        elif choice==5:
            print('-------成功退出--------')
            break
        else:
            print('输入错误请重新输入！')




print('*'*40)
print('\t图书管理')
print('*'*40)

choice=input('新用户注册请输入“1”,登录请输入“2”:')
if choice==1:
    register()
    login()
        
else:
    login()
        
    
books()