def func():
    a=100

    def inner_func1():
        b=90
        s=a+b
        print(s)


    def inner_func2():
        inner_func1()
        print('-------->inner_func2')

    return inner_func2

#调用func

f=func()
print(f)

f()