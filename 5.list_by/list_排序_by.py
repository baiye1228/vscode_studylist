ran_list=[]
import random
for i in range(10):
    ran=random.randint(0,50)
    ran_list.append(ran)
print(ran_list)

# 排序  sorted()  默认升序
# sorted(list)---->默认升序  1 2 3 4 5
# sorted(list,reverse=True)---->降序  5 4 3 2 1
new_list1=sorted(ran_list)
print(new_list1)

new_list2=sorted(ran_list,reverse=True)
print(new_list2)