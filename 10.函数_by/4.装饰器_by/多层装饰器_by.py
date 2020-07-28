def decorate1(func):
    print('------->1 start')

    def wrapper(*args,**kwargs):
        func()
        print('刷漆')

    print('-------> end')
    return wrapper


def decorate2(func):
    print('------->2 start')

    def wrapper(*args,**kwargs):
        func()
        print('铺地板，装门.....')

    print('-------> end')
    return wrapper



#使用装饰器
@decorate2
@decorate1
def house():
    print('我是毛坯房。。。')

house()

'''
装饰器是多层，距离近的先进行
'''