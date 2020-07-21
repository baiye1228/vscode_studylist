# and(与) or(或) not(非)

#逻辑运算符的运算结果返回Ture  False

''' and
左             右
true   and    true   ---->true
true   and    false  ---->false
false  and    true   ---->false
false  and    false  ---->false

'''
n1=8
n2=5
n3=3
result=n1>=(n2+n3) and n1>n2
'''
步骤：
1.n1>=(n2+n3)   8 >= 8   True
2. n1>2    8>5    True
3. true   and   true
4.结果：True

'''
print(result)


''' or
左             右
true   and    true   ---->true
true   and    false  ---->true
false  and    true   ---->true
false  and    false  ---->false

'''
#判断是否存在用户
username=''
email='1234567@qq.com'
result= username=='admin123' or email=='1234567@qq.com'
#       False               or    true    ---->true
print('or--->',result)


# not
flag=False
result= not flag   #取反
print('not--->',result)