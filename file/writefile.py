# 列表中每个字符出现的次数
a=[1,3,3,4,5,5,6,6,7,3]
# set(a)    去重用集合
# print(set(a))
for i in set(a):
    print(a.count(i))

# 一段话中每个单词出现的个数
a="I like the way you s have, hhh with you, 'I' have never envied anyone I I I I"
b=a.replace(',','')      # 替换句子中的“,”号
c=b.replace("'",'').split(' ')    # 替换句子中的“‘”
# b=a.replace(',','').split(' ')
print(set(c))
for i in set(c):
    print('每个单词出现的次数'+i+'为',c.count(i))





