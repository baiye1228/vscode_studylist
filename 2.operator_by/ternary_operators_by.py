# 格式:   结果   if  表达式  else  结果
a=6
b=5
result= (a+b) if a<b else (b-a)
print(result)
'''
判断表达式是Ture还是False
如果Ture则将if前面的内容进行运算，并将结果赋值成result
如果是False则将else后面的内容运算结果，并将结果赋值成result
'''

username=''
# python:判断的变量是''  0   None  默认是False
# python:如果变量有值，例：'abdf' 'afkajh' 认为是Ture
if username:
    print('嘿嘿！我登陆了')
print('-----------')

num=9
if num:
    print('---->',num)
    