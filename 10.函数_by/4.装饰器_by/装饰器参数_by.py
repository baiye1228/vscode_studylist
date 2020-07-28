#登录校验
'''

import time

def decorate(func):
    
    def wrapper():
        print('正在校验中......')
        time.sleep(2)
        print('校验完毕......')
        func()
    return wrapper





@decorate
def f1():
    print('-------f1--------')

@decorate
def f2():
    print('-------f2--------')

f1()
f2()

'''

import time

def decorate(func):
    
    def wrapper(x):
        print('正在校验中......')
        time.sleep(2)
        print('校验完毕......')
        func(x)
    return wrapper





@decorate
def f1(n):
    print('-------f1--------',n)

f1(5)

@decorate
def f2(name):
    print('-------f2--------',name)

f2('lily')

@decorate
def f3(students):
    for stu in students:
        print(stu)

students=['lily','tom','lucy']
f3(students)