'''
异常:因代码的逻辑或者语法上的错误而导致的程序中断
try...except... --- 将可能发生异常的语句放到try语句下面,
如果异常发生程序不会中断,会继续执行except下面的语句
try---except---else---
只要try语句没有错误,输出try下面代码,(也)才执行else语句
try___except___finally___
不论执行try还是except,都执行finally
'''

# try:
#     print(a)
# except:
#     print('hello')


# try:
#     print(a)
# except NameError: #捕获指定异常a
#     print('hello')


# try:
#     f = open('bb.txt','r')
# except NameError: #捕获指定异常(只能捕获命名错误异常)
#     print('hello')



# try:
#     f = open('bb.txt','r')
# except (NameError,FileNotFoundError): #捕获多个指定异常
#     print('hello')



# try:
#     print(a)
#     f = open('bb.txt','r')
# except (NameError,FileNotFoundError)as a:  #获取报错的具体信息
#     print('hello')      #hello
#     print(a)            #name 'a' is not defined



# try:
#     print(1/0)
# except Exception as a:  #捕获所有异常的描述信息
#     print('hello')      #hello
#     print(a)            #错误原因:division by zero



# try没有报错 执行try和else下面的语句    try报错执行except下面的语句
# try:
#     print('1/0')        #1/0
# except Exception as a:
#     print('hello')
#     print(a)
# else:
#     print('ok')         #ok



# try:
#     print('1/0')        #1/0
# except Exception as a:
#     print('hello')
#     print(a)
# else:
#     print('ok')         #ok
# finally:
#     print('都会执行')    #都会执行



# import time
# try:
#     f = open('a.txt') #不写参数默认读取
#     try:
#         while True:
#             con = f.readline()
#             if len(con) == 0:
#                 break
#             time.sleep(2)
#             print(con)
#     except:
#         print('程序异常终止')
#     finally:
#         f.close()
#         print('文件已关闭')
# except:
#     print('文件不存在!!!')






# old_name = input('请输入备份的文件名')
# dian = old_name.rindex('.')
# if dian > 0:
#     new_name = old_name[:dian] + '备份' + old_name[dian:]
#     try:
#         old_f = open(old_name,'rb')
#         new_f = open(new_name,'wb')
#         while True:
#             con = old_f.read(1024)
#             new_f.write(con)
#             if len(con) == 0:
#                 break
#         old_f.close()
#         new_f.close()
#     except:
#         print('文件不存在')
# else:
#     print('输入文件无效')