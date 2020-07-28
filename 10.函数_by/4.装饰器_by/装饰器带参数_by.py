def outer(a):   #第一层：负责接收参数

    def decorate(func): #第二层：负责接收函数

        def wrapper(*args,**kwargs): #第三层：负责接收函数的参数
            func(*args)
            print('----->铺地板{}块'.format(a))

        return wrapper
    return decorate


@outer(10)
def house(time):
    print('我{}拿到房子的钥匙，是毛坯房。。。'.format(time))

house('2020-7-28')