# + 合并 (支持 1.字符串 2.列表 3.元组)
# a='123'
# b='qwer'
# print(a+b)      #123qwer
# c=a+b
# print(c)        #123qwer

# a=['123',234]
# b=['qwe',456]
# print(a+b)        #['123', 234, 'qwe', 456]
#
# a=('123',234)
# b=('qwe',456)
# print(a+b)          #('123', 234, 'qwe', 456)
#
# * 复制 (支持 1.字符串 2.列表 3.元组)
# a='*'
# print(a * 3)            #***
#
# a=['*',1,2,3,]
# print(a * 3)            #['*', 1, 2, 3, '*', 1, 2, 3, '*', 1, 2, 3]
#
# a=('*',1,2,3,)
# print(a * 3)            #('*', 1, 2, 3, '*', 1, 2, 3, '*', 1, 2, 3)
#
# in    not..in... --- 判断某个数据在不在...里 (字符串 列表 元组 集合 字典)
# a='qwert'
# print('q' in a)             #True
# print('q' not in a)         #False
#
# a=['qwert',1,2,3]
# print('q' in a)             #False
# print('q' not in a)         #True
#
# a=('qwert',1,2,3)
# print('q' in a)             #False
# print('q' not in a)         #True
#
# a={'qwert',1,2,3}
# print('q' in a)             #False
# print('q' not in a)         #True
#
# a={'name':'tom','age':18}
# print('name' in a)            #True
# print('tom' in a)             #False  只能判断'键'是否存在
# print('tom' in a.values())    #True values 判断值是否在字典里面
