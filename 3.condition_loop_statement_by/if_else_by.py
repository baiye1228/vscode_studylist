'''
练习：
如果年龄大于18  并且  输入用户名，则打印xxx今年xxx岁

'''
age=int(input('输入年龄：'))
username=input('输入用户名：')

if age>18 and username:
    print('{}今年{}岁了！'.format(username,age))

print('----game over ----')

'''
需求：
  消消乐
   lv1
   lv2
lv1:免费玩 随便玩
lv2:充值  买道具  继续玩
'''
print('*'*10,'欢迎来到消消乐','*'*10)
level=input('请输入你的级别(lv1,lv2):')
if level=='lv1':
    print('免费玩，随便玩！')
else:
    print('已进入付费级别，充值继续玩!')
    money=int(input('请充值(必须为100的整数)：'))
    if money%100==0 and money>0:
        print('充值成功！充值金额为：',money)
    else:
        print('充值失败，充值金额必须为100的倍数！')
#  注意缩进