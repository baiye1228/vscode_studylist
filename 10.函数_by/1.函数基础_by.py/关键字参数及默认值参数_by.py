#关键字参数：key=value

def add(a,b=10):   #关键字参数
    result=a+b
    print(result)

#调用
add(5)

add(4,7)  #此时7会覆盖原来b的默认值


def add1(a,b=10,c=4):
    print(a,b,c)
    result=a+b+c
    print(result)

add1(1)

add(1,5)  #给b赋值成功

#给c赋值
add1(2,c=6)


def func(**kwargs):
    print(kwargs)

func() #{}

func(a=1) #{'a':1}

func(a=1,b=2)  #{'a':1,'b':2}

dict1={'a':10,'b':2,'c':67,'d':7}
func(**dict1)
'''
将字典拆包：
func(a=10,b=2,c=67,d=7)
将字典拆包成关键字参数的形式
'''

def bb(a,b,*c,**d):
    print(a,b,c,d)

bb(1,2)  # 1 2 () {}
bb(1,2,3,4) # 1 2 (3,4)  {}
bb(1,2,x=100,y=100) # 1 2 () {'x':100,'y':200}
bb(1,2,3,x=100) # 1 2 (3,) {'x':100}