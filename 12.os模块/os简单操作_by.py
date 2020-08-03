#模块：os.py
'''
os.path:
    os.path.dirname(__file__)    获取当前文件所在文件目录（绝对路径）
    os.path.join(path,'  ')      返回一个拼接后的新路径

'''

import os

print(os.path)


path=os.path.dirname(__file__)  #获取当前文件所在文件目录（绝对路径）
print(type(path))
print(path)


with open(r'F:\vscode\code_list\study_list\文件操作副本01_by\text001.txt','rb') as stream:
    container=stream.read()  #读取文件内容
    print(stream.name)
    file=stream.name
    filename=file[file.rfind('\\')+1:]

    path=os.path.dirname(__file__)
    path1=os.path.join(path,filename)

    with open(path1,'wb') as wstream:
        wstream.write(container)