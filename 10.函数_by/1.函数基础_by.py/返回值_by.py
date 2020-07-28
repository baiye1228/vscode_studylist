def add(a,b):
    result=a+b
    print(result) #仅限于打印在终端上，辅助查看，但是外部是无法使用的
    return result

x=add(2,6)
print(x)


def add01(a,b):
    result=a+b
    print(result)
    return 1,2,3

x=add01(2,3)
print(x)   #返回多个参数，会将多个参数先放入一个元组中，将元组作为整体返回 x--->(1,2,3)