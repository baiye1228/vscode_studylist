'''
猜大小：
1.系统产生一个数
2.键盘输入一个数
3.将键盘输入的数与系统产生的随机数进行比较

'''
import random    #import  导入   导入随机数函数
num_computer=random.randint(1,10)
print('系统随机数为：',num_computer)
num_person=int(input('系统已在1和10间生成随机数，请输入你的数：'))
if num_person==num_computer:
    print('恭喜成功！获得大奖！')
else:
    print('很遗憾，你输了')