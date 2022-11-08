'''
模块 --- 是一个.py文件,是一类函数,或者类的集合
包 --- 是一个目录,是一类模块的集合,每个包里面都有__init__.py的文件
'''
#导入模块的几种方式
#1.import 模块名 --- 模块名.函数名
# import os
# print(os.listdir())


# 2.from 模块名 import 函数名 --- 函数名()
# from os import rename
# rename('a.txt','aa.txt')
# remove() #没有调用不可使用

#3.from 模块名 import * --- 函数名()
# from os import *
# rename('aa.txt','a.txt')
# print(listdir())

#4.import 模块名 as 别名 --- 别名.函数名()
# import time as ti
# ti.sleep(2)

# #5.from 模块名 import 函数名 as 别名 --- 别名()
# from time import sleep as sl
# sl(5)



#自己创建模块
'''
if __name__=='__main__': --- 判断当前执行的文件是否是本文件
原理:如果__name__在当前文件中,值是__main__,如果在其他文件中被调用,值就变成了被调用的文件名
'''


# import my_module1
# my_module1.testA(4,5)

# from my_module1 import testA
# testA(2,5)

# from my_module2 import testA
# from my_module1 import testA  #有两个模块有相同的函数使用后面的
# testA(2,5)

# import random
# print(random.randint(1,2))

#控制调用哪个函数
# from  my_module1 import *
# testA(1,2)
# testB(5,1)

#调用模块下类里面的方法 --- from 模块名 import 类名
# from my_module1 import A
# aa = A()
# aa.testA(3,2)
# aa.testB(5,2)


'''
包 --- 是一个目录,是一类模块的集合,每个包里面都有__init__.py的文件
'''
#导入调用包里面的模块
#1.import 包名.模块名 ---包名.模块名.函数名()
# import my_package.module1
# my_package.module1.testA()
# import my_package.module2
# my_package.module2.testB()

#2.from 包名 import 模块名 --- 模块名.函数名
# from my_package import module1
# module1.testA()

#3.from 包名.模块名 import 函数名 --- 函数名()
# from my_package.module2 import testB
# testB()

#4.from 包名 import * --- 模块名.函数名()
# '''需要在__init__文件进行添加调用,不添加无法调用
# 调用方式  文件名写入 __all__=['module1','module2']'''
# from my_package import *
# module1.testA()
# module2.testB()

#5.调用包里面的类的方法
#from 包名.模块名 import 类
# from my_package.module1 import A
# aa=A()
# aa.testA()

