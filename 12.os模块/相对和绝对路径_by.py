import os


r=os.path.isabs(r'F:\vscode\code_list\study_list\文件操作副本01_by\text001.txt')
print('----->',r)

r=os.path.isabs(r'..\文件操作副本01_by\text001.txt') #../ 表示返回当前文件的上一级
print('----->',r)

# r=os.path.isabs('images/girl.jpg')  找与文件同级的images里面的girl.jpg

#获取路径

#当前文件所在文件夹路径
path=os.path.dirname(__file__)
print(path)


#获取当前文件的绝对路径
path=os.path.abspath(__file__)
print(path)