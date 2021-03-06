#闭包在函数中的概念：
'''
条件：
1，在外部函数定义了内部函数
2.外部函数是有返回值
3.返回值是：内部函数名
4.内部函数引用了外部函数的变量

格式：
def 外部函数():
    pass

    def 内部函数():
        pass

    return 内部函数


'''

def func():
    a=100

    def inner_func():
        b=99
        print(a,b)
    print(locals())

    return inner_func


x=func()
print(x)

#x就是内部函数，x()就表示调用函数
x()


'''
闭包的作用：
1.可以使用同级的作用域
2.读取其他元素的内部变量
3.延长作用域

闭包总结：
1，闭包优化了变量，原来需要类和对象完成的工作，闭包也可以完成了
2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
3.使代码变得简洁，便于阅读代码
4.闭包是理解装饰器的基础
'''