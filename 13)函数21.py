'''
函数:可重复使用的具有某种功能的代码块
好处:节省代码,重复使用
定义函数: def 函数名(参数):
            代码块...
调用函数: 函数名(参数)   -----函数的调用者
顺序: 先定义 后调用
'''


#封装功能函数
# def gongneng():
#     print('---功能界面---')
#     print('查询明细')
#     print('查询')
#     print('更改密码')
#     print('...')
#     print('----------')
#
#
# #调用函数
# gongneng()
# print('取钱')
# #调用函数
# gongneng()
# print('查询明细')
# gongneng()
# print('更改密码')

# def a():
#     print('hello')
# a()                   #hello


#函数参数的作用

#完成需求如下：一个函数完成两个数1和2的加法运算，如何书写程序
# def a():
#     print(1+2)
# a()

#可以计算任何用户指定的两个数字的和，如何书写程序？
# def jia():
#     a=int(input('输入'))
#     b=int(input('输入'))
#     print(a+b)
# jia()

#位置传参
# def jia(a,b):     #形参  形式参数
#     print(a+b)
# jia(1,4)          #实参  #5

#定义函数,功能是计算任意范围奇数之和
# def he(a):
#     result = 0
#     for i in range(a+1):
#         if i % 2 !=0:
#             result += i
#     print(result)
# he(5)                   #9


'''
              函数返回值的作用
return --- 1.结果赋值：把return后面的数据赋予给函数调用者
            2.函数结束的标志

'''
#1.
# def buy():
#     return'烟'
# #使用变量保存函数返回值
# goods= buy()
# print(goods)

#2.
# def buy():
#     return'烟'
# print(buy())

# def jia(a,b):
#     print(a+b)
# print(jia(1,2))          #none

# def jia(a,b):
#     return a+b
# print(jia(1,2))          #3

# 到 returun结束不再向下执行
# def buy():
#     print('ok')
#     return 'yan'
#     print('hello')
# print(buy())                #ok
#                             #yan


#需求：制作一个计算器，计算任意两数字之和，并保存结果
# def sum_num(a,b):
#     return a+b

# sum = sum_num(1,2)
# print(sum)          #3

# def jia(a,b):
#     return a+b
# print(jia(1,2))       #3


#函数说明文档:能够快速提示这个函数的作用(注释)
# def jia(a,b):
#     """加法运算"""
#     return a+b
# # print(jia(1,2))     #3
# help(jia)         #加法运算



#函数嵌套调用
#所谓函数嵌套调用指的是一个函数里面又调用了另外一个函数




#函数应用
#打印一条横线
# def line():
#     print('-' * 20)
# line()              #--------------------

# #打印五条横线
# def line():
#     print('-' * 20)
# def lines():
#     for i in range(5):
#         line()
# lines()

##打印多条横线
# def line():
#     print('-' * 20)
# def lines(a):
#     for i in range(a):
#         line()
# lines(4)


#函数计算
#求三个数之和
# def a(a,b,c):
#     return a+b+c
# b = a(1,2,3)
# print(b)                      #6

#求三个数平均值
# def sum_num(a,b,c):
#     return a+b+c
# def average_num(a,b,c):
#     sumResult=sum_num(a,b,c)
#     return sumResult / 3
# result = average_num(1,2,3)
# print(result)                   #2.0

# def avg_num(a,b,c):
#     d=(a+b+c)/3
#     return  d
# x=avg_num(1,2,3)
# print(x)