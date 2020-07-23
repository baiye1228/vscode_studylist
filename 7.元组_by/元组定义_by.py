'''
元组
类似列表(当成容器)
特点：
1.定义的符号：()
2.元组中的内容不可修改
3.关键字:tuple

列表       元组
[]         ()
[1]        (1)

'''
t1=()
print(type(t1))  #<class 'tuple'>

t2=('hello')
print(type(t2))
t3=('hello',)
print(type(t3))
t4=('ab','cd')
print(type(t4))

t5=(4,3,2,1,5,6,8,5,3,3)

import random
list1=[]
for i in range(10):
    ran=random.randint(1,20)
    list1.append(ran)
print(list1)

t6=tuple(list1)
print(t6)

#查询：下标  切片
print(t6[0])
print(t6[-1])

#最大值 最小值  求和  求长度
print(max(t6))
print(min(t6))

#元组中的函数：
# index()
# count()
print(t6.count(4))
print(t6.index(4)) #从元组中找出4的下标位置，没有保存