#文件备份
#1.输入目标文件的名字
# old_name = input('请输入备份的文件名')
# # print(old_name)
# #2.规划备份文件的名字 --- 老大名字+备份+后缀
# dian = old_name.rindex('.')
# if dian > 0:
#     # print(old_name[:dian])     #获取最后一个点之前的数据
#     # print(old_name[dian:])     #获取最后一个点之后的数据
#     new_name = old_name[:dian] + '备份' + old_name[dian:]
#     print(new_name)
#     #备份文件,写入数据
#     old_f = open(old_name,'rb') #rb二进制读取
#     new_f = open(new_name,'wb') #wb二进制写入
#     while True:
#         con = old_f.read(1024)   #一次读1024个字节
#         new_f.write(con)         #再将1024个字节写入
#         if len(con) == 0:        #直到读取数量还有0时停止
#             break
#     old_f.close()
#     new_f.close()
# else:
#     print('输入文件无效')




#文件和文件夹的操作
#os --- 与操作系统交互
#os.函数名
import os
#1.rename() ---  文件重命名
# os.rename('a.txt','aa.txt')
#2.os.remove() --- 删除文件
# os.remove('aa.txt')
#3.mkdir() --- 创建文件夹
# os.mkdir('aaa')
#4.rmdir() --- 删除文件夹
# os.rmdir('aaa')
#5.getcwd() --- 获取当前路径
# print(os.getcwd())          #获取了 不打印不显示
#6.chdir() --- 切换路径
# os.chdir('D:\code1')
# print(os.getcwd())            #D:\code1
# os.mkdir('bbb')             #在code1下创建了 bbb 这个文件夹
#7.listdir() --- 获取目录下所有文件的文件名 以列表的形式展现
# print(os.listdir())             #不写获取当前目录
# print(os.listdir('D:\code1'))   #()路径 获取路径下目录的文件名

#需求:批量修改文件的名字
# for i in os.listdir():
#     new_name='python_' + i
#     os.rename(i,new_name)
#修改回来
# for i in os.listdir():
#     new_name = i.replace('python_','')
#     os.rename(i,new_name)



#无关
# import time
# f = open('a.txt','r',encoding='utf-8')
# while True:
#     data = f.read(4)
#     time.sleep(2)
#     print(data)
#     if data ==0:
#         break
#     # print(f.read(3))
