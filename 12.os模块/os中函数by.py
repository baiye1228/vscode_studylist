import os,time

dir1=os.getcwd()
print(dir1)


result=os.listdir(r'F:\vscode\code_list\study_list\文件操作副本01_by')
print(result)  #返回指定目录下所有文件及文件夹，保存到列表中


#创建文件夹

f=os.mkdir(r'F:\vscode\code_list\study_list\文件操作副本03_by')
print(f)



time.sleep(3)
#删除文件夹
f=os.rmdir(r'F:\vscode\code_list\study_list\文件操作副本03_by')
print(f)


#切换目录
f=os.chdir(r'F:\vscode\code_list\study_list\文件操作副本02_by')
print(f)

path=os.getcwd()
print(path)