'''
for 变量名 in 集合:
    语句
'''
print(range(8))  # range(0,8)  包含0 但不包含8  0，1，2，3，4，5，6，7

#  range(n)  ---> 0~n-1
#  range(m,n) ---> m~n-1
#  range(m,n,step)  step 步长
for i in range(0,50,5):
    print('----->',i)


#打印三次
for i in range(3):
    print('hello----->',i)



name='白也'
num=int(input('请输入需要的馒头的数量：'))

for i in range(num):
    print('{}很饿，正在吃第{}个馒头'.format(name,i+1))
else:
    print('还没有给馒头，{}饿哭了。。。'.format(name))
print('-'*20)
'''
for...else..
适用于for循环执行完或没有循环数据时，需要做的事
for i in 范围：
   有数据时执行的语句
else；
   没有数据执行的语句
'''


#用户账号密码登录而且只能登陆三次，如果三次未成功账户锁定
# break 关键字

for i in range(3):
    username=input('请输入用户名：')
    password=input('请输入密码：')
    print(i)
    if username=='baiye' and password=='123456':
        print('欢迎用户:{}'.format(username))
        print('----轻松购物吧----')
        break
    else:
        print('用户名或密码错误！')
else:
    print('账户被锁定，需要重新激活！')