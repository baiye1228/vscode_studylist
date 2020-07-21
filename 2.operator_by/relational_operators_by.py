# ==  !=  >=  <=  >  <  is   is not
n1=int(input('请输入第一个数：'))
n2=int(input('请输入第二个数：'))
#判断n1和n2的大小
result=n1>n2
print('n1>n2:',result) # 结果False  Ture

# is  用于对象的比较
age=20
age1=20
print(id(age))
print(id(age1))
print(age is age1)