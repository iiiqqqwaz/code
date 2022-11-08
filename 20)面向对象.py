'''
面向对象:将函数分类和封装,使开发更高效
面向过程:按照业务逻辑从上往下 书写代码
类:就有相同特征和行为事务的统称(属性即变量,方法即函数)
对象:具有某种功能的个体
类和对象的关系:用类创建一个对象(用类取实例化一个对象)
__init__()作用:用来定义初始化对象属性
            特点:创建对象时自动调用,不需要手动调用
__str__()作用:将打印的对象的内存地址,替换成了return后面的数据
'''

# #1.定义类 --- class 类名():
# class Xiyiji:
#     def xiyifu(self):
#         print('洗衣服')
# #2.实例化对象 --- 对象名 = 类名()
# haier = Xiyiji()
# #3.调用类里面的方法 --- 对象名.方法名()
# haier.xiyifu()

# class Xiyiji:
#     def xiyifu(self):
#         print('洗衣服')
#         print(self)
# haier = Xiyiji()
# print(haier)
# haier.xiyifu()

# self --- 也是类的实例对象,方便在类的内部调用属性和方法
# class A():
#     def tastA(self):
#         print('hello world')
#     def taseB(self):
#         #在类的内部调用方法---self.方法名()
#         self.tastA()
# aa = A()
# aa.taseB()



# class Xiyiji:
#     def xiyifu(self):
#         print('洗衣服')
# haier = Xiyiji()
# haier1 = Xiyiji()
# print(haier)
# print(haier1)
# # 在类的外部添加对象属性 --- 对象名.属性名=值
# haier.gao = 300
# haier.kuan = 200
# haier.xiyifu()
# haier1.xiyifu()
# #在类的外部调用对象属性 --- 对象名.属性名
# print(haier.gao)
# print(haier.kuan)



# class Xiyiji:
#     def xiyifu(self):
#         print('洗衣服')
#     def print_info(self):
#         #在类的内部调用对象属性 --- self.属性名
#         print(self.gao)
# haier = Xiyiji()
# haier1 = Xiyiji()
# haier.gao = 300
# haier.kuan = 200
# haier.xiyifu()
# haier1.xiyifu()
# haier.print_info()




'''__init__()作用:用来定义初始化对象属性
            特点:创建对象时自动调用,不需要手动调用
    __str__()作用:将打印的对象的内存地址,替换成了return后面的数据
'''

# class A():
#     def __init__(self,gao,kuan):
#         # 在类的内部添加(对象属性) --- self.属性名=值,是被该类所有方法所共用
#         self.a=gao
#         self.b=kuan #对象属性
#         self.sum=0
#         self.sum1=0
#     def print_info(self):
#         print(self.a)
#         # self.b+=1
#         print(self.b)
#     def testB(self):
#         print(self.a)
#         print(self.b)
#     def jishuhe(self):
#         for i in range(1,11,2):
#             self.sum+=i
#         print(self.sum)
#     def oushuhe(self):
#         for i in range(0,5,2):
#             self.sum1+=i
#         print(self.sum1)
#     def jia(self,h,k):
#         # print(h+k)
#         return h+k
#     def __str__(self):
#         return '说明书'
#
# aa = A(100,200)
# bb = A(300,400)
# print(aa)
# print(bb)
# aa.print_info()
# bb.print_info()
# print(aa.jia(1,2))
# aa.testB()
# aa.print_info()
# aa.jishuhe()
# aa.oushuhe()

