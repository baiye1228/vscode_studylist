#生成器  generator

'''
得到生成器的方式：
1.通过列表推导式得到生成器


'''


newlist=[x*3 for x in range(20)]
print(newlist)

#得到生成器
g=(x*3 for x in range(20))
print(type(g))


#方式1：通过调用__next__()得到元素
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())


#方式2：next(生成器对象)  系统内置
print(next(g))
print(next(g))