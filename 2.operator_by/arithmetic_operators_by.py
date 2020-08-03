# * / + - 算术运算符
# 扩展的算术运算符 ：**  //  %
a=8
b=2
result=a*b
print('乘法运算：',result)

result=a/b
print('除法运算：',result)

b=3
result=a**b
print("'**'运算：",result)  # b=3  a=8  result=8*8*8=512

result=a//b
print("'//'运算：",result) #取整：2

result=a%b
print("'%'运算：",result) #取余：2

print('*'*50)


a=int(input('输入a:'))
b=int(input('输入b:'))

result=a*b
print(result)
