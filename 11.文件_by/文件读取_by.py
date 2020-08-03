'''
读：
open(path/filename,'rt')------>返回值：stream(管道)

注意：

'''


stream=open(r'F:\vscode\code_list\study_list\11.文件_by\text01.txt')


container=stream.read()
print(container)


result=stream.readable()   #判断是否可读
print(result)


line=stream.readline()
print(line)