#1.增加：
dict1={}

#格式：dict1[key]=value   key唯一  value不唯一
#特点：同名则会覆盖   无同名则添加

dict1['brand']='huawei'
print(dict1)  #{'brand':'huawei'}

dict1['brand']='mi'
print(dict1)

dict1['type']='p30 pro'
dict1['price']=9000
dict1['color']='黑色'
print(dict1)

'''
案例：
用户注册功能

username
password
email
phone
'''

print('-----------欢迎来到站双帕弥什用户注册------------')
database=[]
while True:
    username=input('输入用户名：')
    password=input('输入密码：')
    repassword=input('输入确认密码：')
    email=input('输入邮箱：')
    phone=input('输入手机号：')
    user={}
    user['username']=username
    if password==repassword:
        user['password']=password
    else:
        print('两次密码不一致！')
        continue
    user['email']=email
    user['phone']=phone
    #保存到数据库
    database.append(user)
    answer=input('是否继续注册？(y/n):')
    if answer!='y':
        break
print(database)