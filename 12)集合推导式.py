#创建一个集合 数据为下方列表的二次方
#1.
# a=[1,1,3]
# b=set()
# for i in a:
#     b.add(i**2)
# print(b)    #{1, 9}  集合不会重复数据

#2.
# a=[1,1,3]
# c={i**2 for i in a}
# print(c)