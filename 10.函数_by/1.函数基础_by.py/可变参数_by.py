#定义方式:

def add(*args):
    sum1=0
    if len(args)>0:
        for i in args:
            sum1+=i
        print('累加的和为：',sum1)
    else:
        print('无元素可计算，sum1=0')

add()
add(1,2)
add(1,2,3,4)