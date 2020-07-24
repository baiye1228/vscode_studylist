#update()  []+[]  合并操作

dict1={0:'tom',1:'jack',2:'lucy'}
dict2={0:'lily','4':'ruby'}

result=dict1.update(dict2)
print(result)
print(dict1)

#formkeys(sq) ----->将seq转成字典的形式，如果没有指定默认的value则用None   如果指定default,则default替代None这个value值


list1=['aa','bb','cc']
new_dict=dict.fromkeys(list1,10)
print(new_dict)