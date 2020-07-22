'''
列表支持的符号：
+
*
in
'''

# +
l1=[1,2,3]
l2=[5,6,7]
l3=l1+l2
print(l3)

# *
l4=[5,8]*3
print(l4)

# in
result=3 in [1,2,3,4]
print(result)

'''
列表中的元素：
整型
字符串类型
浮点型
列表
元组
字典
对象
'''
result=[3,2] in [1,2,[3,2],4]
print(result)

# [[1,2],[4,5,6,7]] 二维
l5=[[1,2],[3,2,1],[4,5],[7,3,1]]
print(len(l5))

e=l5[2]
print(e,type(e)) #[4,5]
print(e[1])

print(l5[1][1])

'''
类型转换：
str()
int()
list() 将指定的内容转成列表
iterable 可迭代的

'''
print(list(range(1,10,3)))

s='abc'
print(list(s))