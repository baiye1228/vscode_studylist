def func(a,*args,**kwagrs):
    print(a,args,kwagrs)

t=(1,2,3,4)
func(1,t)  # 1 ((1,2,3,4),)

l=[2,5,8]
func(1,l,c=9,b=6)  # 1  ([2,5,8],)  {'c':9,'b':6}

dict1={'1':'a','2':'b','3':'c'}
func(1,*l,**dict1)


'''
courses=['html','mysql','python']
'''

def fun01(name,*args):
    if len(args)>0:
        for i in args:
            print('{}学过了{}'.format(name,i))
    else:
        print('没学过任何编程知识!')

courses=['html','mysql','python']

fun01('baiye',*courses)