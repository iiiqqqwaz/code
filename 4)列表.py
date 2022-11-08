'''
列表(list)
格式:以中括号为标识,数据与数据之间用逗号隔开
定义列表:变量名 = [值,'值',.......]    变量名 = list(数据)
特点 1.可变的
    2.支持索引
    3.支持切片
'''
# a = [1,2,3,4,'qwer']
# print(type(a))
# print(a[2])         #3
# print(a[-1])        #qwer
# print(a[-1][0])     #r


# a = [1,2,3,4,'qwer','3',3]
# print(type(a))         #list
# print(a[2])            #3
# print(a[-3])           #qwer
# print(a[-3][0])        #q
# #index() --- 获取某个数据的下标
# print(a.index('qwer')) #4
# #count() --- 统计某个词在数据中有几个
# print(a.count(3))      #1
# print(a.count('3'))    #1
# #len() --- 统计变量中有多少数据
# print(len(a))          #7
# #in：判断指定数据在某个列表序列，如果在返回True，否则返回False
# #in not...in... --- 判断某个数据在不在...里面
# print('qwer' in a)     #True
# print(1 in a)          #True
# print('n' in a)        #False



#添加的三种方式       (append     extend    insert)
#append()--- 往列表中添加新的数据 默认添加到结尾,只能添加一个
# b = [1,2,3,4,'qwer','3',3]
# b.append(5)
# print(b)
# b.append([5,6])  #尾部添加一个整体小列表
# b[-1].append([7])  #小列表中的末尾添加7
# print(b)

#extend()---往列表结尾添加数据 插入的数据被拆分添加 合并列表
# a=[1,2,3,4,'qwer']
# # a.extend('qwer')
# # print(a)
# a.extend(['qwer','ert'])
# print(a)

#insert() --- 往指定的下标位置添加数据
# a=[1,2,3,4,'qwer']
# a.insert(3,999)   #3是下标位置添加新的数据999  (下标,新的数据)
# print(a)
# a.insert(2,[111,222])   #添加也可以添加列表
# print(a)



#删除 del()      pop()        remove()      clerr()
#del --- 删除     del[下标] 删除某一个数据
# a=[1,2,3,4,'qwer']
# # del a  #删除列表
# del a[4]   #删除a列表 下标为4的数据
# print(a)

#pop() --- 根据下标删除某个数据
# a=[1,2,3,4,'qwer']
# a.pop(3)             #删除下标为3的数据
# # print(a.pop(3))    #print(a.pop(3))可以反馈删除的数据
# print(a)
# print()

# #remove() --- 删除指定的某一个数据,如果有相同的只能删除一个指定数据
# a=[1,2,3,4,'qwer','qwer']
# a.remove('qwer')
# print(a)                       #[1, 2, 3, 4, 'qwer']

#clear() --- 清空列表
# a=[1,2,3,4,'qwer']
# a.clear()
# print(a)                    #[]


#修改
#根据下标进行修改:变量名[下标] = 新值
# a=[1,2,3,4,'qwer']
# a[1] = 5
# print(a)                       #[1, 5, 3, 4, 'qwer']

#逆置:将数据反过来
# a=[1,2,3,4,'qwer']
# a.reverse()
# print(a)                     #['qwer', 4, 3, 2, 1]


#sort() --- 排序 从小到大,正序排列
# a=[1,3,2,6,3]
# a.sort()
# print(a)                    #[1, 2, 3, 3, 6]

#排序 方法1:从大到小,倒序显示 (先排序,后[sort]逆置)
# a=[1,3,2,6,3]
# a.sort()
# a.reverse()
# print(a)                  #[6, 3, 3, 2, 1]

#从大到小排序 方法2:
# a=[1,3,2,6,3]
# a.sort(reverse=True)
# print(a)                  #[6, 3, 3, 2, 1]



#copy() --- 复制
# a=[1,2,3,4,'qwer']
# print(a.copy())         #[1, 2, 3, 4, 'qwer']
# b=a.copy()
# print(b)                #[1, 2, 3, 4, 'qwer']


