import os

# a = os.popen('ipconfig')  # 执行cmd命令
# print(a.read())
# print(os.getcwd())
# os.chdir(r'd:\code1')
# print(os.getcwd())
# print(os.listdir('d:/'))
# os.remove('百度2.html')     #删除文件


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
#8. 执行cmd命令
# a = os.popen('ipconfig')
# print(a.read())
#9. 添加递归目录
# os.makedirs('aaa/bbb/ccc')
#10. 删除递归目录
# os.removedirs('aaa/bbb/ccc')

#!!!注意:路径分割不判断文件是否存在
#11.将路径与文件名分隔开
# print(os.path.split('d:/code/ccc.txt'))
##('d:/code', 'ccc.txt')
#12.将路径和文件后缀名分隔开
# print(os.path.splitext('d:/code/ccc.txt'))
##('d:/code/ccc', '.txt')
#13.将盘符与路径分隔开
# print(os.path.splitdrive('d:/code/ccc.txt'))
##('d:', '/code/ccc.txt')

#14.判断文件是否是一个目录 --- 结果为bool值
print(os.path.isdir('d:/code'))         #True
print(os.path.isdir('d:/code/ccc.txt')) #False
#15.判断文件是否是一个普通文件 ---结果为bool值
print(os.path.isfile('d:/code'))        #False
print(os.path.isfile('d:/code/ccc.txt'))#True
print(os.path.isfile('d:/code/zzz.txt'))#文件不存在仍为False
#16.判断路径下存不存在某个目录或文件
print(os.path.exists('d:/code/ccc.txt'))#True
print(os.path.exists('d:/code/荣耀图片'))#True
print(os.path.exists('d:/code/不存在的文件.目录'))#False
#17.文件重命名
#剪切
os.rename('d:/code/ccc.txt','d:/code1/zzz.txt')