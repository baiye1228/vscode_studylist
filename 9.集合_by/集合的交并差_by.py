set1={2,3,4,5,6}
set2={2,3,4,5,6,7}

#差集：-    difference()

set3=set2-set1
print(set3)

set4=set2.difference(set1)
print(set4)


# 交集：&    intersection()
set5=set2 & set1
print(set5)

set6=set2.intersection(set1)
print(set6)


#并集：|    union()联合
set7=set1|set2
print(set7)


#对称差集  symmetric_different()
s1={5,1,2,9,0,3}
s2={2,5,7,9}
result=(s1|s2)-(s1&s2)
print(result)

result=s1^s2
print(result)