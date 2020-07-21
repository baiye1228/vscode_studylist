#查找相关的，替换
# find() rfind() lfind() index() rindex() lindex() replace()


s1='index lucy lucky goods'

result='x'in s1
print(result)

position=s1.find('R')  #返回值是-1则代表没找到
print(position)

position=s1.find('l')  #如果可以找到则返回字母第一次出现的位置
print(position)

# find('要查找的字符',start,end)
p=s1.find('o',position+1,len(s1)-5)    #也可以指定开始位置查找
print(p)


# https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png

ur1='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'

p=ur1.rfind('/')  # right find  从右侧检索/的位置
print(p)

filename=ur1[p+1:]
print(filename)

'''
index同find()用法，查找不到会报告异常
'''


#替换
s2=s1.replace(' ','#')
print(s2)