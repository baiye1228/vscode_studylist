#定义函数:随机数的产生

import random



def generate_random(number):
    for i in range(number):
        ran=random.randint(1,20)
        print(i,ran)

print(generate_random)

#调用：函数名()
generate_random(number=int(input('输入:')))