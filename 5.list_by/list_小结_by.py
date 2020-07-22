'''
列表函数：只有通过列表才能调出来的函数

添加   append  extend insert
删除   del list(index)
       remove()  删除列表中第一次出现的元素e,返回值是None  如果没有找到则报告异常
       pop()     弹栈  移除列表中最后一个元素 返回值为删除的元素  默认是删除最后一个   也可指定下标删除
       clear()   清除列表

翻转：reverse()   逆序改变列表

'''
hotpot_list=['海底捞','呷哺呷哺','张亮麻辣烫','热辣一号','宽板凳']

hotpot_list.append('张亮麻辣烫')
print(hotpot_list)

result=hotpot_list.remove('张亮麻辣烫')
print(result)
print(hotpot_list)


hotpot_list.pop()
print(hotpot_list)

hotpot_list.reverse()
print(hotpot_list)