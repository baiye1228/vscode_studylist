# isalpha()  是否是字母   isdigit()  是否是数字
s='abcd'
result=s.isalpha()
print('result--->',result)

s='6688'
result=s.isdigit()
print('result--->',result)


sum=0
i=1
while i<=3:
    num=input('请输入数字:')
    if num.isdigit():
        num=int(num)
        sum+=num
        print('第{}个数字累加成功！'.format(i))
        i+=1
    else:
        print('不是数字！')
print('sum=',sum)