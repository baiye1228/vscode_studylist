#赋值运算符
#1.=
name='baiye'
#将'baiye'的值赋给变量name
name1=name
print(id(name),name)
print(id(name1),name1)#节省内存，有点像C++的指针，赋值是一种内存指向的改变
print(name==name1)

#扩展后的赋值符号   +=   -=   *=   /=  ...
num=8
num+=5  # num=num+5  此时+为数学加号
print(num)

a='abc'
a+='ff'  #等价于： a=a+'ff'  此时+为连接符  包含：1.连接  2.连接后的结果
print(a)
# -=  *=   /=  仅运用于数值运算，不适用于字符串