def func():
    try:
        n1=int(input('输入数字：'))
        print(n1)
        return 1

    except ValueError:
        print('必须是数字。。。')
        return 2
    else:
        print('输入完毕！！')  #无异常则执行