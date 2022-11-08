# """
# 局部变量 --- 在函数中定义的变量是局部变量在局部范围内(函数内部)有生效
# 全局变量 --- 在函数内外都生效的变量
# global 变量名 --- 将 局部变量变成全局变量
# """
#
# #局部变量 ---函数体内部变量
# def testA():
#     a = 100  #变量a在函数内部
#     print(a)
# print(a)  # 报错
# testA()   #100
#
#
# #全局变量 --- 函数体外部变量
# a=100
# def testA():
#     print(a-1)
# def testB():
#     print(a)
# testA()     #99
# testB()     #100
# print(a)    #100
#
# #修改testB的a值变成200
# #全局变量 --- 函数体外部变量
# a=100
# def testA():
#     print(a)
# def testB():
#     a=200        #局部变量
#     print(a)
# testA()     #99
# testB()     #200
# print(a)    #100



# #global函数
# a=100
# def testA():
#     print(a)
# def testB():
#     global a     #将testB里面的A由局部变量变成全局变量
#     a=200        #局部变量
#     print(a)
# testA()     #100
# testB()     #200
# print(a)    #200


# #先调用哪个函数就先执行哪个函数下面的代码
# a=100
# def testA():
#     print(a)
# def testB():
#     global a     #将testB里面的A由局部变量变成全局变量
#     a=200        #局部变量
#     print(a)
# testB()     #200
# testA()     #200
# print(a)    #200
#
#
# #返回值的参数传递
# def test1():
#     return 50
# def test2(num):
#     print(num)
# #1.保存函数test1的返回值
# result = test1()
# #2.将函数返回值所在变量作为参数传到test2函数

# test2(result)

# #函数的返回值
# def test1():
#     return 1   #return 结束的标识
#     return 2
# print(test1())


# def test1():
#     return 1,2   #返回1和2 默认为元组格式set()
#     return 2
# print(test1())


