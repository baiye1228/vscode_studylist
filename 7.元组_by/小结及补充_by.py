'''
符号：
+
*
is    not is
in    not in

系统函数：
max()
min()
sum()
len()
sorted()  ---->排序，返回的结果就是列表
tuple()   ---->元组类型的强制转换

元组内置函数：
index()
count()

拆装包：
x,*y=(1,2,3,4,5)
print(y)
print(*y)
'''

t2=(3,4)+(1,2)
print(t2)

t3=(3,4)*2
print(t3)

print(t2 is t3)

print(3 not in t3)

print(len(t2))

print(tuple(sorted(t2)))