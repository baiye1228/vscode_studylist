#产生10个随机数，将其保存到列表中
'''
步骤：
1.如何产生随机数
2.10个数字产生
3.将产生的随机数放到列表中
4.打印列表
'''
ran_list1=[]
import random
for i in range(10):
    ran=random.randint(0,50)
    ran_list1.append(ran)
print(ran_list1)

#产生10个不同的随机数
ran_list2=[]
i=0
while i<10:
    ran=random.randint(0,20)
    if ran not in ran_list2:
        ran_list2.append(ran)
        i+=1
print(ran_list2)

#找出列表中的最大值  max(list)--->列表中的最大值
max_list2=max(ran_list2)
print(max_list2)

max_list1=ran_list1[0]
for value in ran_list1:
    if value>max_list1:
        max_list1=value
print('最大值为：',max_list1)

#找出列表中的最小值  min(list)--->列表中的最小值
min_list2=min(ran_list1)
print(min_list2)
print(min(ran_list1))

#求和  sum(list) 系统求和函数
sum1=0
for i in range(10):
    sum1+=ran_list1[i]
print(sum1)