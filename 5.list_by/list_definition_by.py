#声明
names=['jack','tom','lucy','superman','ironman']

computer_name=[]

#地址
print(id(names))
print(id(computer_name))

#获取第一个元素
print(names[0])
print(names[-5])

#获取最后一个元素
print(names[-1])
print(names[4])

#结合循环
print('*'*20)
for name in names:
    print(name)


#查询元素
for name in names:
    if name=='superman':
        print('有超人在里面！')
        break
else:
    print('没有超人在里面！')


if 'superman' in names:
    print('有超人在里面！')
else:
     print('没有超人在里面！')