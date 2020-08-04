#列表推导式  字典推导式  集合推导式
#旧的列表------>新的列表

#列表推导式：格式：[表达式 for 变量 in 旧列表]  或者  [表达式  for  变量  in  旧列表  if  条件]




#过滤掉长度小于或等于3的人名
names=['tom','lucy','abc','jack','steven','bob','ba']

result=[name for name in names if len(name)>3]
print(result)

#将1-100之间能被3和5整除，组成一个新的列表
newlist=[i for i in range(100) if i%3==0 and i%5==0]
print(newlist)



dict1={'name':'tom','salary':6000}
dict2={'name':'lucy','salary':8000}
dict3={'name':'jack','salary':4500}
dict4={'name':'lily','salary':3000}

list1=[dict1,dict2,dict3,dict4]

#如果薪资大于5000加200，如果薪资小于5000加500
newlist=[emplovee['salary']+200 if emplovee['salary']>5000 else emplovee['salary']+500 for emplovee in list1]
print(newlist)