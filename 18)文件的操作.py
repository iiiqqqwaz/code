'''
对文件的操作
1.打开文件 --- open(name,mode)
2.操作 --- r w a  读 写 追加
3.关闭文件 --- close()
encoding='utf-8' 可以输入中文
'''

#变量名 = open(name,mode,encoding='utf-8')
# f = open('a.txt','w',encoding='utf-8')
# #变量名.write('内容')
# f.write('小明')
# #变量名.close() --- 关闭文件(释放内存)
# f.close()

#with 语句 自动关闭  不需要写.close关闭语句
#with open(name,mode,encoding='utf-8')as 变量名:
    #代码

# with open('a.txt', 'r', encoding='utf-8')as f:
#     print(f.read())


#r --- 读取,表示只读 如果文件不存在则报错
f = open('a.txt','r',encoding='utf-8')  #读存在的文件
print(f.read())
f.close()

# #打开路径下文件的操作
# f = open(r'D:\code1\111.txt','r',encoding='utf-8')  #r转意 或者用双\\ 或者/
# print(f.read())
# f.close()

#w --- 写入，表示只写   如果文件不存在 先创建 再写入 执行写入会覆盖原有的内容
# f = open('b.txt','w',encoding='utf-8')
# f.write('aaa')
# f.close()

#a --- 追加,文件不存在 先创建文件并追加
# f = open('D:/code1/c.txt','a',encoding='utf-8')
# f.write('qqq')
# f.close()

'''
read() --- 如果不加参数就是读取文件中的所有内容 类型为字符串
readlines() --- 读取文件中的所有内容,结果是列表
readline() --- 每次只读取文件中的一行,本身具有累加功能,类型为字符串
'''
# f = open('c.txt','r',encoding='utf-8')
# print(f.read())         #read()输入几读取多少个字节,换行符也算一个字节
# print(type(f.read()))  #结果是字符串类型
# f.close()

# f = open('c.txt','r',encoding='utf-8')
# print(f.readlines())             #['qqq\n', 'cqq']
# print(type(f.readlines()))       #结果是列表类型
# f.close()

# f = open('c.txt','r',encoding='utf-8')
# print(f.readline())             #qqq
# print(f.readline())             #cqq
# print(type(f.readline()))       #结果是字符串类型
# f.close()

#如何删除换行符
# f = open('c.txt','r',encoding='utf-8')
# data = f.readlines()
# f.close()
# print(data)
# list1=[]
# for i in data:
#     ii = i.replace('\n','')   #i是循环过一个又一个 c.txt里面的单行的数据 将i的换行符变成空赋给变量ii
#     list1.append(ii)          #向空列表list1添加没有换行符的变量ii
# print(list1)


#向文件中写入20行内容 最后一行不换行
# f = open('c.txt','w',encoding='utf-8')
# for i in range(20):
#     if i >= 19:
#         f.write('qqq')
#     else:
#         f.write('qqq'+'\n')
# f.close()