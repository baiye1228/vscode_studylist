# dictionary 字典
'''
字典：
    特点：
    1.符号：{}
    2.关键字：dict
    3.保存的元素：  key:value

列表       元组       字典
[]         ()          {}
list       tuple      dict
ele        ele       key:value

element  元素

'''

dict1={}  #空字典

dict2=dict()  #空字典

dict3={'ID':'21713247578471823','name':'lucy','age':18}

#  dict4=dict(('name','lucy'))
dict4=dict([('name','lucy'),('age',18)])
print(dict4)

dict5=dict([(1,2),(4,5),(6,8),(9,0)])
print(dict5)
#注意：list可以转成字典 但前提是：列表中的元素都要成对出现