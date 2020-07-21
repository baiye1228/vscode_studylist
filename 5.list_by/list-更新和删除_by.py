brands=['hp','dell','thinkpad','支持华为','lenovo','mac','神州']

print(brands)
print('----------------------------')


#更改
for i in range(len(brands)):
    #i是0，1，2，3...--->下标
    if '华为'in brands[i]:
        brands[i]='huawei'
        break
print(brands)


#删除  del
del brands[2]
print(brands)

#删除 只要是hp ,mac 都要删除
print('--------------------------')
l=len(brands)
i=0
while i<l:
    if 'hp' in brands[i] or 'mac' in brands[i]:
        del brands[i]
        l-=1
    i+=1
print(brands)