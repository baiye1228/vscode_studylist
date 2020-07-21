'''
输入两个字符串，从第一字符串中删除第二个字符串中所有字符
例：输入“They are students.”和“aeiou”
则删除之后的第一个字符串变成了“Thy r stdnts.”
'''
s1=input('请输入第一个字符串：')
s2=input('请输入第二个字符串：')
for i in range(len(s2)):
    key2=s2[i]
    for j in range(len(s1)):
       key1=s1[j]
       if key1==key2:
           s1=s1.replace(key1,'')
           break
print(s1) 

#例答
s1=input('请输入第一个字符串：')
s2=input('请输入第二个字符串：')
s3=''
for i in s1 :  #类似range(len(s1))
    if i not in s2:
        s3+=i
print(s3)

'''
for i in s2:
    s1=s1.replace(i,'')
print(s1)
'''