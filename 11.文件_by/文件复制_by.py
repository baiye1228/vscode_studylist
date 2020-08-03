'''
with 结合open使用可以帮助我们自动释放资源
    如果文件不存在，则自动创建

'''

with open(r'F:\vscode\code_list\study_list\11.文件_by\text01.txt','rb') as stream:
    container=stream.read()

    with open(r'F:\vscode\code_list\study_list\11.文件_by\测试复制.txt','wb') as wstream:
        wstream.write(container)

print('文件复制成功！')