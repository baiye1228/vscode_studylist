#写文件

'''
mode是“ w ” 表示就是写操作
      “ a ” 表示追加操作

方法：
     write(内容)   每次都会将原来内容清空，然后写当前内容

    writelines(Iterable)   没有换行效果


'''



stream=open(r'F:\vscode\code_list\study_list\11.文件_by\text02.txt','a',encoding='utf-8')

s='''
你好：
    欢迎来到澳门博彩赌场，赠送你一个金币！
       赌神：高进
'''


result=stream.write(s)
print(result)

stream.write('龙五')

stream.close()