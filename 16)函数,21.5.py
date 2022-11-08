#拆包元组
# def testA():
#     return 100,200
# a , b= testA()
# print(a)
# print(b)

#拆包字典
# a={'name':'tom','age':20}
# b,c = a
# # print(b)
# # print(c)
# print(a[b])
# print(a[c])
#
# #交换变量值
# #有变量a= 10 和 b= 20，交换两个变量的值
# a=10
# b=20
# a,b=b,a
# print(a)
# print(b)
#借助第三变量
# a=10
# b=20
# c=0
# c=a
# a=b
# b=c
# print(a)        #20
# print(b)        #10

'''
lambda 匿名函数
格式:函数名 = lambda 参数:表达式
lambda 函数一般只用于只有一个表达式的函数,不能处理复杂的具有逻辑结构的函数
'''
# def he(a,b):
#     return a+b
# print(he(2,3))        #5

# he = lambda x,y : x+y
# print(he(2,3))          #5

#高阶函数 abs    打印出一个数的绝对值(绝对值负数为正数,正数为正数)
# print(abs(-10))         #10

# def he(a,b):
#     return abs(a) + abs(b)
# print(he(1,-2))        #3

# print(round(1.5))   #round四舍五入

# def he(a,b,c):
#     return c(a) + c(b)
# print(he(1.5,+2.3,round))        #4