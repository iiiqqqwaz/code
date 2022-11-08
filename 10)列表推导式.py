#列表推导式   --- 把控制语句写进列表中,使产生的结构直接存在在列表中
#需求:创建一个0-10的列表
#1.
# a=[]
# for i in range(11):
#     a.append(i)
# print(a)
#
# #列表推导式   简化
# #2.
# b=[i for i in range(11)]
# print(b)
#
# #将0-10的偶数创建为一个列表
# # 1.
# a=[]
# for i in range(0,11,2):
#     a.append(i)
# print(a)            #[0, 2, 4, 6, 8, 10]
#
# #2.
# a=[]
# for i in range(0,11):
#     if i %2 ==0:
#       a.append(i)
# print(a)            #[0, 2, 4, 6, 8, 10]
#
# #3.
# b=[i for i in range(0,11) if i%2 == 0]
# print(b)            #[0, 2, 4, 6, 8, 10]
#
#
# #输出:[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# #1.
# b=[]
# for i in range(1,3):
#     for j in range(3):
#         b.append((i,j))
# print(b)
#
# #2.
# c=[(i,j)for i in range(1,3) for j in range(3)]
# print(c)