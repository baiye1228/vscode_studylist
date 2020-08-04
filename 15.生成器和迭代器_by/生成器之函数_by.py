g=(x*3 for x in range(20))

while True:
    try:
        e=next(g)
        print(e)
    except:
        print('没有更多元素了！')
        break

#定义生成器的方式2：借组函数完成
#只要函数中出现了yield，说明函数就不是函数了，变成了生成器



#斐波那契数列

def func():
    n=0
    while True:
        n+=1
       # print(n)
        yield n

g=func()
print(g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))




#斐波那契数列

def fib(lenght):
    a,b=0,1
    n=0

    while n<lenght:
       # print(b)
        yield b
        a,b=b,a+b
        n+=1

g=fib(8)

print(next(g))
print(next(g))