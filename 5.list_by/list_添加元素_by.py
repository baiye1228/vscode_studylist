# list列表的添加：
#临时的小数据库：


#列表的函数：append  extend   insert

# append()  末尾追加
girls=['杨幂']

'''
while True:
    name=input('请输入你心目中的美女名字：')
    if name=='quit':
        break
    girls.append(name)
print(girls)
'''

#extend  类似列表的合并
names=['小月月','王丽坤']

# girls.extend(names)

print(girls)

girls=girls+names
print(girls)


#  insert 插入
#  ['杨幂', '小月月', '王丽坤']
#     0        1        2
girls.insert(1,'刘涛')
print(girls)