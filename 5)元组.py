'''
元组(tuple)
格式:以小括号为标识 数据与数据之间用 逗号 隔开
定义元组:变量名 = (值,'值',....)   将其他的数据类型转换为元组 变量名=tuple(数据)
特点: 1.不可变
     2.支持索引
     3.支持切片
注意: 如果元组中只有一个数据 结尾处必须加逗号才为一个元组
'''

# a = (1,2,3,'234')
# #1)index() --- 获取某个数据的下标
# print(a.index('234'))       #3
# #2)count() --- 统计某个数据的个数
# print(a.count('234'))       #1
# #3)len() --- 统计元组中有多少数据
# print(len(a))               #4
# #4)in  not...in  --- 判断某个数据在不在...里
# print(1 in a)               #True
# print(11 not in a)          #True

# a = (1,2,3,[6,7,8,9],'234')
# a[3][0]=1
# print(a)

