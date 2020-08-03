import os

#文件复制

src_path=r'F:\vscode\code_list\study_list\文件操作副本01_by'
target_path=r'F:\vscode\code_list\study_list\文件操作副本02_by'

#封装成函数
def copy(src,target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist=os.listdir(src)

        for file in filelist:
            path =os.path.join(src,file)
            with open(path,'r') as rstream:
                container=rstream.read()
                path1=os.path.join(target,file)
                with open(path1,'w') as wstream:
                    wstream.write(container)

        else:
            print('复制完毕！')


copy(src_path,target_path)
