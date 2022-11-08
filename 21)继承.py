#单继承 --- 一个子类会继承一个父类下的所有属性和方法
#多继承 --- 一个子类继承多个父类的时候,默认继承括号里面第一个父类
#方法重写 --- 子类有父类的同名属性和方法会重写同名的属性和方法
#私有属性和方法不能被继承也不能在类的外部被使用:只能在类的内部使用
# class A():
#     def __init__(self):
#         self.a = 100
#     def testA(self):
#         print(self.a)
# class B(A):
#     pass
# bb = B()
# bb.testA()
# print(bb.a)

#师傅类
# class Master():
#     def __init__(self):
#         self.kongfu='古法配方'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #徒弟类
# class Tudi(Master):
#     pass

# daqiu = Tudi()
# daqiu.make_cake()
# print(daqiu.kongfu)


# 师傅类
# class Master():
#     def __init__(self):
#         self.kongfu='古法配方'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #学校类
# class School():
#     def __init__(self):
#         self.kongfu='博文配方'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #徒弟类
# class Tudi(School,Master):   #默认继承第一个
#     pass
# daqiu = Tudi()
# daqiu.make_cake()
# print(daqiu.kongfu)

#方法重写
#daqiu掌握了师父培训的技术后，自己潜心钻研出自己的独门配方的一套全新的煎饼果子技术。
# 师傅类
#方法重写
#daqiu掌握了师父培训的技术后，自己潜心钻研出自己的独门配方的一套全新的煎饼果子技术。
# 师傅类
# class Master():
#     def __init__(self):
#         self.kongfu='古法配方'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #学校类
# class School():
#     def __init__(self):
#         self.kongfu='博文配方'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #徒弟类
# class Tudi(School,Master):
#     def __init__(self):
#         self.kongfu='独创配方'
# daqiu = Tudi()
# daqiu.make_cake()
# print(daqiu.kongfu)  #调用到重写后的



#多层继承
# class Master():
#     def __init__(self):
#         self.kongfu='古法配方'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #学校类
# class School():
#     def __init__(self):
#         self.kongfu='博文配方'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #徒弟类
# class Tudi(School,Master):
#     def __init__(self):
#         self.kongfu='独创配方'
# #徒孙类
# class Tusun(Tudi):
#     pass
#
# xiaoqiu = Tusun()
# xiaoqiu.make_cake()
# print(xiaoqiu.kongfu)

#私有权限
# class Master():
#     def __init__(self):
#         self.kongfu='古法配方'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #学校类
# class School():
#     def __init__(self):
#         self.kongfu='博文配方'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #徒弟类
# class Tudi(School,Master):
#     def __init__(self):
#         self.kongfu='独创配方'
#         #添加私有属性--- self.__属性名 = 值
#         self.__money = 2000000  #私有属性不被继承
#     #添加私有方法
#     def __siyou(self):
#         print('hello')
#     #获取私有属性
#     def get_money(self):
#         print(self.__money)
#         self.__siyou()
#     #修改私有属性
#     def set_money(self,a):
#         self.__money = a
#
# #徒孙类
# class Tusun(Tudi):
#     pass
#
# xiaoqiu = Tusun()
# xiaoqiu.make_cake()
# # print(xiaoqiu.kongfu)
# daqiu = Tudi()
# daqiu.set_money(1000)
# daqiu.get_money()


# class A():
#     def work(self):
#         print('指哪打哪')
#
# class B(A):
#     def work(self):
#         print('追查毒品')
#
# class C(A):
#     def work(self):
#         print('追击敌人')
#
# def test(a):
#     a.work()
#
# bb = B()
# cc = C()
# test(cc)
# test(bb)

#类属性
class A():
    #添加类属性 --- 属性名 = 值
    tooth = 10
    def __init__(self):
    #在类的内部添加对象(实例)属性 --- self.属性名 = 值
        self.bb = 100
    def testA(self):
        print(A.tooth)
        print(self.tooth)
        print(self.bb)
''' '类'属性可以被类对象和该类的实例化对象调用
    '(实例)'属性 只能被该类的实例化对象调用,不能被类对象调用
    类属性只能通过类对象修改 不能通过实例化对象修改'''
wangcai = A()
xiaohei = A()


A.tooth=20            #类属性修改
wangcai.tooth = 30      #对象属性  创建对象属性 重新定义
print(A.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)
wangcai.testA()
# print(A.bb)      #bb是实例属性 不能被类调用
print(wangcai.bb)
print(xiaohei.bb)

