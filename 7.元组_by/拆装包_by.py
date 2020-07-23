t1=(4,7,3)

a,b,c=t1
print(a,b,c)

a=t1
print(a)

#变量个数与元组个数不一样

t1=(2,5,8,9,7)
a,*_,c=t1
print(a,c,_)

a,c,*_=t1
print(a,c,_)

a,b,*c=t1
print(a,b,c)

a,*b=t1
print(a,b)
print(b)
print(*b)

t2=(9,)
a,*b=t2
print(a,b)