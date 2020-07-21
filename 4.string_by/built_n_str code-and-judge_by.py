#字符串内建函数：encode 编码   decode 解码     网络应用（中文一般会涉及编码问题）

#编码
msg='上课啦！认真听课！'

# gbk 中文   gb2312 简体中文  unicode

result=msg.encode('utf-8')
print(result)

#解码
m=result.decode('utf-8')
print(m)


#字符串内建函数：startswith()  endswith()  返回值都为bool类型

# startswith()判断是否是以xxx开头    endswith()判断是否是以xxx结尾

#例应用：  文件上传   只能上传图片（jpg,png,bmp,gif)
filename='笔记.doc'
result=filename.endswith('doc')
print(result)

s='hello'
result=s.startswith('he')
print(result)