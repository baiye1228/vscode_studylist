'''
小易喜欢的单词具有以下特性：
1.单词的每个字母都是大写
2.单词没有连续相等的字母
'''
word=input('请输入一个单词：')
for i in range(len(word)):
    if word[i]<'A' or word[i]>'Z':
        print('不喜欢！不是大写！')
        break
    else:
        if i<len(word)-1 and word[i]==word[i+1]:
            print('不喜欢！是叠词！')
            break
else:
    print('喜欢！') 