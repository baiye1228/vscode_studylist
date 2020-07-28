'''
加入购物车   付款   修改收货地址
判断用户登录状态



'''

def func(number):
    a=100

    def inner_func():
        nonlocal a
        for i in range(number):
            a+=1

        print('修改后的a:',a,i)

    return inner_func


#调用func
d=func(5)
d()

#函数作为参数
a=50
f1=func(a)
print(f1)


#地址引用
def text():
    print('-----text------')



def func1(text):
    print(text)
    text()
    print('----------->func1')

'''
特点：
1.函数A是作为参数出现的(函数B接收函数A作为参数)
2.要有闭包特点

'''


#定义一个装饰器

def decorate(func1):
    a=100
    print('wrapper外部打印测试')
    def wrapper():
        func1()
        print('-------->刷漆')
        print('-------->铺地板',a)
        print('-------->装门')

    print('wrapper加载完成.....')
    return wrapper

#使用装饰器
@decorate
def house():
    print('我是毛坯房。。。')

house()

'''
1.house 被装饰函数
2.将被装饰函数作为参数传给装饰器decorate
3.执行decorate函数
4.将返回值又赋值给house
'''