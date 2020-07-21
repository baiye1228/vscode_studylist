#字符串

s1='abc'
s2="abc"
s3='''abc'''
print(id(s1),id(s2),id(s3))  # '''三引号占用的内存空间与单双引号的不同(前提：'''三引号不在同一行上)

print(s1==s2) #比较的是内容
print(s1 is s2) #比较的是地址

print(s2==s3)
print(s2 is s3)

s1=input('请输入：') # 'abc'
s2=input('请输入：') # 'abc'

print(s1==s2)   # True
print(s1 is s2) # False
#常量赋值is是True，input输入底层做了处理所以最后地址是不一样的



#字符串的运算符：+ *
s3=s1+s2
s4=s1*5
print(s3)
print(s4)

# in 在.....里面
name='steven'
result='t' in name #返回值为bool类型
print(result)

# not in 没在...里面
result='tv'not in name #返回值为bool类型
print(result)

# % 字符串格式化
print('%s说：%s'%(name,'hello'))

# r 保留原格式 即有r不发生转义
print(r'%s说：\'哈哈哈\''%name)

#[]
filename='picture.png'
print(filename[5])  # 通过[]可以结合位置 获取字母  特点：只能获取一个字母

#range(1,10) ---类似--->  [1:10]

print(filename[1:7]) #包前不包后
print(filename[3:7]) #截取字符串
#省略
print(filename[:7])  #只要省略后面的数，表示一直取到字符串的末尾
print(filename[3:])  #只要省略前面的数，表示从0开始取值
# 负数
print(filename[8:-1])
print(filename[:-2])
print(filename[-1:])
print(filename[-5:-1])

#[::]
print(filename[::-2]) #倒序输出

str1='abcdefg'
print(str1[-1:-5:-1]) #gfed

'''
str[start:end:方向和步长]
方向： 正数  方向从左向右
       负数  方向从右向左
注意数值顺序：
    例：正向： 5：0  就不行了
        反向： 5：0  就可行
'''
