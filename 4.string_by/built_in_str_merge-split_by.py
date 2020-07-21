# join() : '-'.join('abc')  将abc用-连接构成一个新的字符串

new_str='-'.join('abc')
print(new_str)

list1=['a','v','o','9']
result=''.join(list1)
print(result)

result=' '.join(list1)
print(result)


#  lstrip  rstrip  strip

s='    hello    '
s=s.lstrip()   #去除字符串左侧的空格
print(s+'8')

s=s.rstrip()  #去除字符串右侧的空格
print(s+'8')

s=s.strip()
print(s+'8')

# split()  分割字符串,将分割后的字符串保存在列表中
s='hello world hello kitty'
result=s.split(' ',2)  #表示按空格作为分隔符，分隔字符串两次
print(result)

n=s.count(' ')  # count(args) 求字符串中指定args的个数
print('个数：',n)