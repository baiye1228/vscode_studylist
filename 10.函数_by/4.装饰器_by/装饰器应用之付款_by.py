#开发登录验证

import time
islogin=False  #默认没登陆


#定义一个登录函数
def login():
    username=input('输入用户名:')
    password=input('输入密码:')
    if username=='baiye' and password=='123456':
        return True
    else:
        return False

def decorate(func):
    def wrapper(*args,**kwargs):
        global islogin
        print('--------付款--------')
        #验证用户是否登录
        if islogin:
            func(*args,**kwargs)
        else:
            print('用户没有登录，不能付款!')
            islogin=login()
    return wrapper

@decorate
def pay(money):
    print('正在付款，付款金额：{}元！'.format(money))
    print('付款中...')
    time.sleep(2)
    print('付款成功！')

pay(10000)

pay(8000)