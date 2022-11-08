'''
字典(dict)
以大括号为标识,数据以键值对方式存在
格式:     变量名 = {键:值,......}
特点:     1.可变的
         2.不支持索引切片
         3.根据键来索引对应的值
注意:  字典里面的键都是唯一的
      有两个相同的键默认输出最后一个
'''
#定义空字典
a={}
print(type(a))
a={'name':'tom','age':18}
print(a)        #{'name': 'tom', 'age': 18}
#1)1.根据键索引值---变量名[键]
a={'name':'tom','age':18}
print(a['name'])    #tom
print(a['age'])     #18
#2.get索引键得到对应值
print(a.get('age')) #18
#2)添加新的键值对 --- 变量名[键]=值
a={'name':'tom','age':18}
a['id'] = 6
print(a)            #{'name': 'tom', 'age': 18, 'id': 6}
#3)修改键对应的值 --- 变量名[键]=新值
a={'name':'tom','age':18}
a['name']='小明'
print(a)            #{'name': '小明', 'age': 18}

#4)del del a[键]
a={'name':'tom','age':18}
# del a           #将a这个字典删除
del a['name']   #{'age': 18} 将键为'name'的键值对删除
print(a)

# #5)pop() --- 删除字典里面的键值对
a = {'name':'tom','age':18}
a.pop('age')
print(a)                  #{'name': 'tom'}

#6)keys() --- 获取字典中所有的键
a = {'name':'tom','age':18}
print(a.keys())         #dict_keys(['name', 'age'])

#7)values() --- 获取字典中所有的值
a = {'name':'tom','age':18}
print(a.values())        #dict_values(['tom', 18])
print(list(a.values()))  #['tom', 18]
for i in a.values():
    print(i)             #tom
                         #18

# #8)items() --- 获取字典中所有的键值对
# a = {'name':'tom','age':18}
# print(a.items())            #dict_items([('name', 'tom'), ('age', 18)])
# #循环遍历
# for i in a.items():
#     print(i)                #('name', 'tom')
#                             #('age', 18)
# #分别将字典中的键,值输出出来
for i,j in a.items():
    print(i)            #i 输出字典中的键    name \n tom
    print(j)            #j 输出字典中的值    age  \n 18