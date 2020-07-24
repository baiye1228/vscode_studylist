list1=[3,5,6,7]
del list1[1]
print(list1)

dict1={'张三':100,'李四':100,'王五':89,'赵六':99}
del dict1['王五']
print(dict1)

# del dict1['hahaha']  报错

#字典的内置函数：删除
# pop(key[,default])  ----->根据key删除字典中的键值对，返回值是  只要删除成功，则返回值对的值value

result=dict1.pop('李四')
print(result)
print(dict1)

result=dict1.pop('张晓','没有对应值')
print('====>',result)

#popitem():随机删除字典中的键值对（一般是从末尾删除元素）

#clear() --->同列表的clear()