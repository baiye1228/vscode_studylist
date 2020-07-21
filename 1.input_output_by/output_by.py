movie='进击的巨人'
ticket=45.3
count=35
total=ticket*count
print('电影：%s'%movie,'\n人数：%d'%count)
message='''
电影：%s
人数：%d
单价：%f
总票价：%.1f

'''%(movie,count,ticket,total)
print(message)

age=2
message='乔治说：我今年{}岁了'.format(age)
print(message)