i=0
while i<=10:
    print(i)
    i+=1
print('打印完毕！')



# 打印 9*9 乘法表
ceng=1
while ceng<=9:
    count=1
    while count<=ceng:
        rel=count*ceng
        print(' {}*{}={} '.format(ceng,count,rel),end='')
        count+=1
    ceng+=1
    print()