# 字符串的内建函数：声明一个字符串，默认可以调用内建函数（系统准备好的一些函数）

#大小写
# capitalize() title() istitle() upper() lower()

message='zhaorui is a beautiful girl!'

msg=message.capitalize() #将字符串的第一个字符转成大写的表示形式
print(msg)

msg=message.title() #返回的是 每个单词的首字母大写的字符串
print(msg)

result=msg.istitle() # bool类型
print(result)

msg=message.upper() #将字符串全部转成大写的表示形式
print(msg)

msg=msg.lower()    #将大写全部转成小写
print(msg)


#案例:验证码

s='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
print(len(s)) #求字符串长度  len(str) ,返回一个整型的数值
code=''
import random

for i in range(4):
    ran=random.randint(0,len(s)-1)
    code+=s[ran]

print('验证码：',code)
user_input=input('请输入验证码：')
if user_input.lower()==code.lower():
    print('验证码输入正确！')
else:
    print('验证码错误！')