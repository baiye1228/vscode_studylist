'''
集合：
set   关键字    无序不重复的元素
作用：
    不重复的特点
'''
list1=[1,2,4,5,7,6,2,34,54,3,3,2]
s1=set()
s2={1,3,7}

print(type(s1))
print(type(s2))

#应用:列表的快速去重
s3=set(list1)
print(s3)

#添加 add()  添加一个元素


s1.add('hello')
s1.add('lucy')
print(s1)

t1=('林志玲','李荣浩')
s1.update(t1)
print(s1)

#删除： remove  pop   clear
# dicard() 类似于 remove()  在移除不存在的元素时不会报错

s1.remove('李荣浩')
print(s1)

s1.pop()   #随机删除{一般删除第一个}
print(s1)