#异常处理
'''
格式：
try:
    可能出现异常的代码

except:
    如果有异常执行的代码
[Finally:
    无论是否存在异常都会被执行的代码]
'''

def run():
    try:
        n1=int(input('输入第一个数字：'))
        n2=int(input('输入第二个数字：'))

        per=input('输入运算符号(+ - * /):')

        result=0
        if per=='+':
            result=n1+n2
        elif per=='-':
            result=n1-n2
        elif per=='*':
            result=n1*n2
        elif per=='/':
            result=n1/n2
        else:
            print('输入的符号有误！！')
            
        print('结果是：',result)

    except ZeroDivisionError:
        print('除数不能为0！！！')
    except ValueError:
        print('必须输入数字！！！')

run()
print('---------->')


'''
异常情况1：
try:
    有可能出现多种异常

except 异常类型1：
    pass

except 异常类型2：
    pass
except Exception:
    pass

异常情况2：获取Exception的错误原因
try:
    有可能出现多种异常

except 异常类型1：
    pass

except 异常类型2：
    pass
except Exception as err:
    print(err)

'''