'''
掷骰子
1.欢迎进入游戏
2.输入用户名，默认用户没有币
3.提示用户充值卖币（100元30币，充值必须是100的倍数，充值不成功可以再次充值）
4.玩一局游戏扣除2个币，猜大小（系统用随机数模拟骰子产生值）
5.猜对了奖励3个币，可以继续玩（用户无币时或不足以支付一局游戏时提醒充值或退出游戏）
'''

print('------------欢迎进入游戏-----------')
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
game_money=0
print('您的账户余额为0，请充值！')
while game_money==0:
    money=int(input('充值金额：'))
    if money%100==0:
        game_money=money//100*30 
        print('恭喜您充值成功！游戏币余额：{}'.format(game_money))
        break
    else:
        print('请您充值100的倍数的金额')
ju=0
while game_money>=2:
    ju+=1
    print('--------------开始您的第{}局游戏-------------'.format(ju))
    game_money-=2
    import random
    num_computer=random.randint(1,6)
    num_person=int(input('您猜"大"或"小"（大请输入1，小请输入0：'))
    if num_computer>=1 and num_computer<=3 and num_person==0:
        game_money+=3
        print('掷的数为：{}，所以是小！恭喜您获得3个游戏币，您现在的余额：{}'.format(num_computer,game_money))
    elif  num_computer>=4 and num_computer<=6 and num_person==1:
        game_money+=3
        print('掷的数为：{}，所以是大！恭喜您获得3个游戏币，您现在的余额：{}'.format(num_computer,game_money))
    else:
        print('很遗憾！您猜错了！您现在的余额：{}'.format(game_money))
print('余额不足！欢迎下次游玩！')