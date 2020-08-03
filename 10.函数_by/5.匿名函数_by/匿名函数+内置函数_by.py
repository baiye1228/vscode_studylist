list1=[3,4,8,2,9,0]
m=max(list1)

print('列表最大值：',m)


list2=[{'a':10,'b':20},{'a':34,'b':19},{'a':23,'b':17}]

m=max(list2,key=lambda x:x['a'])
print('列表最大值：',m)


# map

list3=[3,4,6,2,9,7,2]

result=map(lambda x:x+2 ,list3)
print(list(result))


# reduce()  对可迭代中的元素进行加减乘除运算的函数
from functools import reduce

tuple1=(2,3,5,1,5,6,4,7,9)

result=reduce(lambda x,y:x+y ,tuple1)

print(result)


tuple2=(1,)
result=reduce(lambda x,y:x+y ,tuple2,10)
print(result)


#filter()
list4=[3,46,5,2,7,634,234,7,45,24]

result=filter(lambda x:x>10 ,list4)
print(list(result))