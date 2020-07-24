'''
修改：
list1[index]=newvalue

dict1[key]  =newvalue

查询元素:
list1[index] ---->element

dict1[key]   --->value

'''
list1=[3,5,7,8]
print(list1[2]) #列表中找元素根据下标

dict1={'1':'张三','2':'李四','3':'王五'}
print(dict1['2']) #字典中找元素根据key

dict2={'张三':100,'李四':100,'王五':89,'赵六':99}
print(dict2['王五'])

#考试分数大于90分的人
#尝试对字典遍历
for i in dict2:
    print(i)

#单独遍历字典的结果是：字典的key

#字典里的函数： items()    values()   keys()


# items
print(dict2.items())

for key,value in dict2.items():
    if value>90:
        print(key)

#values:取出字典中所有值，保存到列表中
result=dict2.values()
print(result)

#求所有学生的平均分
for score in dict2.values():
    print(score)

scores=dict2.values()
total=sum(scores)
avg=total/len(scores)
print(avg)

#keys()  获取字典中所有的key键  （键值对）

names=dict2.keys()
print(names)

#找人： in   也可用于字典操作   用于判断元素有没有在字典的key中出现
'''
1.根据key获取值，如果在字典中没有存在则报出keyError
 dict[key] ---->value
2.字典中的内置函数：
get(key)  ----->  如果取不到值则不会报错，则返回None
get(key,default)  ---->  如果能够取到值则返回字典中的值，如果取不到则返回default的值


'''

print('王五' in dict2)
print(dict2.get('赵飞',99))
