#

a=100  #全局变量

def func():
    b=99

    def inner_func():
        global a
        nonlocal b
        c=88
        #尝试打印
        print(a,b,c)

        c+=12
        b+=1
        a+=10
        print(a,b,c)
    inner_func()

func()