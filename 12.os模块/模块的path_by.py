import os

path=os.path.abspath(__file__)
print(path)


result=os.path.split(path)
print(result)
print(result[1])  #获取文件名


result=os.path.splitext(path)
print(result)   #获取文件的扩展名


size=os.path.getsize(path)
print(size)     #获取文件大小   单位：字节