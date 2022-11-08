#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Time : 2022/8/9 9:17
# @File : 3)字符串.py
# @Software: PyCharm


'''
字符串:一串字符的集合
定义一个字符串:   变量=值     变量名=str(值)
字符串的特点:1.不可变的 2.支持索引 3.支持切片
索引:根据下标位置取对应的数据叫做索引,下标首位从0开始----变量名[下标号]
切片:获取字符串中的某一部分数据----变量名[开始截取下标:结束位置的下标:步长]'''
# a='bowen'
# b='zhisheng'
# print(type(a))
# print(type(b))
# a='bowen'\
#     'zhisheng'
# print(a)
# c='''qqq
# qq'''
# print(c)
# b="i'm tom"
# print(b)
# a = 'i\'m tom'
# print(a)

# a = 'qwerty'
# print(a[0])     #q
# print(a[3])     #r
# print(a[-1])    #y

# a='0123456789'
# print(a[3])
# print(a[2:5])
# print(a[:5])   #01234  如果不写开始 默认下标从0开始选取
# print(a[1:])    #如果不写结束 表示选取到最后
# print(a[:])     #选取所有
# print(a[::2])   #从开始到结束 步长为2
# print(a[::-1])  #步长为正数 从从左到右开始选取  步长为负数从右往左选取
# print(a[::-2])  #97531
# print(a[-4:-1]) #678
# print(a[-5:-1:-1]) #如果选取的方向和步长发生了冲突
# print(a[-5:-10:-1]) #54321

#变量名.函数名()
# find()获取字符串中某一个数据的下标,如果不存在则反馈-1
# a='qwwwert'
# print(a[2])             #w
# print(a.find('w'))      #1
# print(a.rfind('w'))     #最右边的'w' 从左向右数第 3

# #index() --- 获取字符串中某一个数据的下标，如果不存在则报错
# a = 'qewrtw'
# print(a.index('w'))
# print(a.rindex('w'))

# count() --- 统计字符串中某一个数据有多少个
# a = 'qwewerret'
# print(a.count('e'))
#
# len() 统计字符串中一共有多少个数据
# a = '12345'
# print(len(a))
#
# replace() 替换字符串中某个数据
# a = 'qwerrrrt'
# print(a.replace('r','y'))    # 吧a 里面全部的r 换成Y
# print(a.replace('r','y',2))  #2 从左往右替换2个次数,不可以为负数
# print(a)
#
# split() --- 以某一个数据为分隔符,将字符串分割成列表
# a='qwerty'
# print(a.split('r'))
# b = a.split('r')
# print(a)
# print(b)
#
# c='qwrerty'   #不写字数 全部r进行分割
# print(c.split('r'))
#
# d='qwrertry'  #2是从左向右数两个r进行分割
# print(d.split('r',2)) #['qw', 'e', 'try']

# d='qwrertry' #2是从左向右数两个r进行分割
# print(d.rsplit('r',2)) #['qwre', 't', 'y']

#
# join() --- 字符串拼接,列表，元组，集合   只能拼接字符串不能数字
# a = ['q','w','e']
# print(''.join(a))  #双引号是一个列表  如果想用其他符号连接 ''引号写链接符号
# b=''.join(a)       # 将拼接后的字符串赋予给b这个变量
# print(b)
#
# a = ('q','w','e')
# print(''.join(a))  #双引号是一个列表  如果想用其他符号连接 ''引号写链接符号
# b=''.join(a)       # 将拼接后的字符串赋予给b这个变量
# print(b)
#
#
# capitalize() --- 将字符串中的第一个数据变成大写,如果字符串中有大写则除了第一位全部变成小写
# a = 'qwert'
# print(a.capitalize())
#
# title() -- 将字符串中每一个单词的首字母变成大写,除了首字母全部变成小写
# a='hello world'
# print(a.title())
# b=a.title()
# print(b)
#
# lower()将字符串大写转成小写
# a = 'hElLo'
# print(a.lower())
#
# upper()将字符串中小写转大写
# a = 'heLlo'
# print(a.upper())
#
# 判断 结果:真 or 假
# startswith() --- 判断字符串是否以某个数据开头 结果为bool值
# a = 'qwert'
# print(a.startswith('q'))  #True
# print(a.startswith('w'))  #False
#
# endswith() --- 判断字符串是否以某给数据结尾 结果为bool值
# a = 'qwert'
# print(a.endswith('t'))  #True
# print(a.endswith('w'))  #False