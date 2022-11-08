# print('hello word') #打印输出hello word
# # print('hello word')
#
# '''
# 注释1
# 注释2
# 注释3
# '''
#
# """
#  注释1
#  注释2
#  注释3
# """
#
# '''不换行注释也可以'''
#
# my_name='tom'
# print(my_name)
#
# schoolName='博文智生'
# print(schoolName)
# a=1
# print(a)
# print(type(a))
#
# age=18
# name='tom'
# weight=75.5
# student_id=1
# print('我的名字是%s' % name)
# print('我的学号是%4d' % student_id)

#定义变量 变量名=值
# name='tom'
# a=1
# A=2
# print(name)
# print(a)
# print(A)
# schoolname='博文'
# print(schoolname)

#数据类型
# a=1
# b=1.1
# c=True
# d='12345'
# e=[10,12,30]
# f=(10,20,30)
# h={10,20,30}
# g={'name':'tom','age':20}
# print(type(a))  #<class 'int'>整形
# print(type(b))  #<class 'float'>浮点型
# print(type(c))  #<class 'bool'>布尔型
# print(type(d))  #<class 'str'>字符串
# print(type(e))  #<class 'list'>列表
# print(type(f))  #<class 'tuple'>元组
# print(type(h))  #<class 'set'>集合
# print(type(g))  #<class 'dict'>字典

# age=18
# name='小明'
# weight=75.5
# id=1
# print('我的名字是%s' %name)
# print('我的体重是%.2f' %weight)
# print('我的年龄是%d' %age)
# print('我的学号是%04d' %id )
# print('我的名字是%s' %name,'今年%d岁' %age)
# print('我的名字是%s，我的年龄是%s岁' %(name,age))
# print('我的名字是%s，我的明年是%s岁' %(name,age+1))
# print(f'我的名字是{name}，我的年龄是{age}岁')
# print(f'我的名字是{name}，我的年龄是{age+1}岁')
# print('我的名字是{},我的年龄是{}岁'.format(name,age))
# print('我的名字是{},我的年龄是{}岁'.format(name,age+1))

# print('hello word')
# print('hello\n word')
# print('\t12345')
# print('111',end='\n')  #默认自带换行符
# print('222')
# print('111',end='\t')
# print('222')
# print('111',end='---')
# print('222')

#输入-----input(提示信息)
# passwd=input('请输入密码:')
# print(passwd)
# print(type(passwd))

# age=18
# name='小明'
# weight=75.5
# id=1
#
# print(f'我的名字是{name}\n\t今年{age},\n我的班级是{id}')
# print('我的身高是%.2f' %weight)
# print('我的年龄是%09d' %age)

# a=input('请输入密码')
# print(f'您输入的密码是{a}')
# print(type(a))





#   8.6
#数据类型的抓换
#int() ---整数形
# a=1.1
# b=int(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

#input默认字符串类型 用转义字符可更改
# passwd=int(input('请输入密码:'))
# print(passwd)
# print(type(passwd))

#float 转换为浮点型
# a=1
# b=float(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

#str()---转换为字符串
# a=123
# b=str(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# a={'name':'tom'}
# b=str(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# a=(21,123,321)
# b=str(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

#tuple()---元组
# a='123'
# b=tuple(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# a={'age':12}
# b=tuple(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))
#
# a={1,2,3}
# b=list(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

#set()---转换成集合    集合是无需的
# a=(1,2,3)
# b=set(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))


#eval()将字符串中的数据转换成原本的数据类型
# a='1234'
# b=eval(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# a="[1,2,3,4]"
# b=eval(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))



# a="(1,2,3,4)"
# b=eval(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))


# passwd=int(input('请输入密码'))
# print(passwd)
# print(type(passwd))

# num=input('请输入您的幸运数字')
# print(num)
# print(type(num))
# print(type(int(num)))

#算术运算符
# print(1+1)
# print(3-1)
# print(2*9)
# print(8/2)
# print(8//3)
# print(8%3)
# print(2**5)
# print((1+2)*3)

#赋值运算符
# a=1
# print(a)
#
# b=2
# c=3
# d=4
# print(b)
# print(c)
# print(d)

#多变量赋值
# b,c,d=2,3,4
# print(b)
# print(c)
# print(d)

#多变量赋相同值
# a=b=10
# print(a)
# print(b)

#复合赋值运算符 ----先计算 算数运算符 然后将算数运算符执行的结果 取等号 赋值给等号后面的变量
#c+=a --- c=c+a
# a = 100
# a +=1
# print(a)

# b=2
# b*=4
# print(b)
#
# c=10
# c+=1+2  # c=c+1+2
# print(c)

# c =10
# c*=1+2
# print(c)


#比较运算符
# a =1
# b =2
# print(a == b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a >= b)
# print(a <= b)

#逻辑运算符
# a=1
# b=2
# c=3
# print(a<b and b>c) #and 与 都真才真 有假则假
# print(a>b or b<c) # or 有真则真
# print(not a>b)


# age=20
# if age>=18:
#     print('年纪够了可以上网')
#
# print('系统关闭')

# age=int(input('请输入年龄'))
# if age>=18:
#     print(f'年纪够了{age}可以上网')
# print('系统关闭')

# age=int(input('请输入您的年龄'))
# if age>=18:
#     print(f'您的年龄是{age}，可以上网')
# else:
#     print(f'您的年龄为{age},不满足上网的年龄')
# print('系统关闭')

# age=int(input('请输入年龄'))
# if age<18:
#     print(f'您的年龄是{age}回去上学')
# elif age>=18 and age<=60:
#     print(f'您的年龄是{age}去上班')
# elif age>60:
#     print('退休吧你')


# money=1
# zuowei=1
# if money==1:
#     print('请上车')
#     if zuowei ==1:
#         print('坐下')
#     else:
#         print('站着')
# else:
#     print('跟着车跑')


# #猜拳游戏
# #电脑出拳
# import random
# com = random.randint(0,2)
# #玩家出拳
# player = int(input('玩家请出手势 0-石头 ,1-剪刀 ,2 -布：'))
# #玩家胜利
# if (player==0 and com ==1)or(player == 1 and com == 2)or(player==2 and com==0):
#     print('玩家胜利')
# #平局
# elif player==com:
#     print('平局')
# else:
#     print('电脑胜利')

#三元表达式
# a=1
# b=2
# if a > b:
#     c=a
# else:
#     c = b
# print(c)
#
# #化简
# c = a if a>b else b  #如果a>b 则将a的值赋给C 如果条件不是a>b 则 则把B的值给C
# print(c)

#练习：输入成绩 90-100 优秀 80-90打印良好 70-80打印及格  0-70打印渣渣
#练习：判断闰年 输入年数 判断是否闰年
#闰年：1、能被4整除但是（且）不能被100整除 或  2、能被400整除
# sco=int(input('请输入您的成绩'))
# if 100<=sco<=90:
#     print('优秀')
# elif 80<=sco<=90:
#     print('良好')
# elif 70<=sco<=80:
#     print('及格')
# elif 0<=sco<=70:
#     print('不及格')

# year=int(input('请输入是哪年'))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print('是闰年')
# else:
#     print('不是闰年')

# a=1
# b=2
# print(a>b or a<b)


# print(100%4)
# print(101//4)
