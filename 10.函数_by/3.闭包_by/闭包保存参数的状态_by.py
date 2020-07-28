def func(a,b):
    c=10

    def inner_func():
        s=a+b+c
        print('相加之后的结果是:',s)

    return inner_func

#调用func
ifunc=func(6,9)  #ifunc就是inner_func

ifunc1=func(2,8)

ifunc()
ifunc1()

'''
1.保存返回返回闭包时的状态(外部函数变量)
'''