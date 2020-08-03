'''
1.选择人物
2.购买武器  金币
3.打仗  赢得金币
4.选择和删除武器
5.查看武器
6.退出游戏
'''
print('*'*40)
print('\t欢迎来到王者荣耀')
print('*'*40)

for i in range(3):
    username=input('请输入用户名：')
    password=input('请输入密码：')
    if username=='baiye' and password=='123456':
        print('亲爱的用户 {} 恭喜您登录成功！'.format(username))
        break
    else:
        print('用户名或密码错误！')
else:
    print('您的帐户已锁定，需要激活！')

role=input('请选择英雄(1.鲁班 2.后羿 3.李白 4.孙尚香 5.貂蝉 6.诸葛亮):')
coins=1000

print('欢迎{}来到王者荣耀，当前英雄{}当前金币余额：{}'.format(username,role,coins))

while True:
    choice=input('请选择：\n\t1.购买武器\n\t2.对战\n\t3.武器库\n\t4.退出游戏\n\t您的选择是：')
    if choice==1:
        pass
    elif choice==2:
        pass
    elif choice==3:
        pass
    elif choice==4:
        pass
    else:
        print()