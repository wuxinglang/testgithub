# -*-coding:utf-8-*-
# 100+Python编程题
# 题1
# 1级
# 问题:编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000年至3200年(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。
# 提示:考虑使用range(#begin， #end)方法

# a=[]
# for i in range(2000,3200+1):
#     # print(i)
#     if i%7==0 and i%5!=0:
#         a.append(str(i))
# print(",".join(a))

# print('请输入：')
# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print ("LETTERS", d["LETTERS"])
# print ("DIGITS", d["DIGITS"])
import json
a = '["content-type" , "text/html"]'
b=a.replace("[",'').replace("]",'').replace("\"",'')
b.split(',')
print(type(b))