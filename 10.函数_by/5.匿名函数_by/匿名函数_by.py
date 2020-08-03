#简化函数定义

'''
格式：lambda  参数1，参数2...：运算

'''

s= lambda a,b:a+b

print(s(2,3))


#匿名函数作为参数
def func(x,y,func):
    print(x,y)
    print(func)
    s=func(x,y)
    print(s)

func(1,2,lambda a,b:a+b)