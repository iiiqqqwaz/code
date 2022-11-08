# i=0
# while i < 5:
#     print('我错了')
#     i += 1            #i=i+1
#
# print('任务结束')



#1-5的偶数累加和
# i=1
# leijia=0
# while i<=5:
#     if i % 2 ==0:
#         leijia+=i
#     i +=1
# print(leijia)

# i=0
# result = 0
# while i < 6:
#     result += i
#     i += 2
# print(result)

#break: ----当某些条件成立 退出整个循环
# i = 1
# while i<=5:
#     if i ==4:
#         print('吃饱了')
#         break
#     print(f'吃了第{i}个苹果')
#     i +=1

#continue: ----当某个条件成立 退出当前循环
# i =1
# while i <=5:
#     if i ==3:
#         print(f'大虫子,第{i}个不吃了')
#         i+=1
#         continue
#     print(f'吃了第{i}个苹果')
#     i+=1

#嵌套循环的流程   大循环执行一次 小循环执行一轮
# j = 0
# while j<3:
#     i = 0
#     while i<3:
#         print('我错了')
#         i +=1
#     print('刷碗')
#     j += 1
# print('结束')

# j = 0
# while j < 5:
#     i=0
#     while i<=j:
#         print('*',end='\t')
#         i +=1
#     print()
#     j +=1

# j= 1
# while j<=9:
#     i = 1
#     while i <= j:
#         print(f'{i}*{j}={i*j}',end='\t')
#         i +=1
#     print()
#     j += 1

'''
for 临时变量 in 序列：
    代码块...

序列----字符串,列表，元组，集合，字典，range(数字)
range()----1.括号里面只有一个数字时 标识默认从0开始 到此数字结束但取不到此数字结束
括号里有两个数字时 表示从第一个数字开始 到第二个数字结束, 但取不到第二个数字
括号里有三个数字时 表示从第一个数字开始 到第二个数字结束, 但取不到第二个数字 第三个表示递增
'''

# for i in range(5):
#     print('我错了',end='\t')

#1-100 的累加和
# result = 0
# for i in range(1,101):
#     # print(i)
#     result += i
# print(result)

#1-5偶数累加和
# a=0
# for i in range(1,6):
#     if i % 2 == 0:
#         a+=i
# print(a)

#吃到第三个苹果不吃了
# for i in range(1,6):
#     if i ==4:
#         print('吃饱了不吃了')
#         break
#     print(f'吃了{i}个苹果')

#一共五个苹果 吃到第三个苹果有虫子  然后继续吃
# for i in range(1,6):
#     if i == 3:
#         print('有虫子')
#         continue
#     print(f'吃了第{i}个苹果')


# for j in range(3):
#     for i in range(3):
#         print('我没错')
#     print('刷碗')




#while ...else...
# i = 1
# while i <=5:
#     print('我错了')
#     i+=1
#
# else:
#     print('原谅你了')



#只要循环没有被break掉,就执行else语句
# i = 1
# while i <=5:
#     if i ==3:
#         print('不真诚')
#         break
#     print('我错了')
#     i+=1
# else:
#     print('原谅你了')

# i = 1
# while i <=5:
#     if i ==3:
#         print('不真诚')
#         i+=1
#         continue
#     print('我错了')
#     i+=1
# else:
#     print('原谅你了')

#for....else
#不真诚继续道歉
# for i in range(1,6):
#     if i == 3:
#         print(f'第{i}遍不真诚')
#         break
#     print('我错了')
#
# else:
#     print('原谅你了')

# j= 1
# while j<=9:
#     i = 1
#     while i <= j:
#         print(f'{i}*{j}={i*j}',end='\t')
#         i +=1
#     print()
#     j += 1


# for j in range(1,10):
#     for i in range(1,j+1):
#         print(f'{i}*{j}={i*j}',end='\t')
#     print()


# for j in range(1, 10):
#     for i in range(1, j + 1):
#         print(f'{i}*{j}={i * j}', end='\t')
#         # i += 1
#     print()
#     # j += 1

# i=1
# r=0
# while i<=100:
#     r+=i
#     i+=1
# print(r)

# sum=0
# for i in range(1,100):
#     sum = sum + i
# print(sum)



# result = 0
# for i in range(1, 100):
#     if i % 2 != 0:
#         result += i
#     elif i % 2 == 0:
#         result -= i
# print(result)

# import random
# com = random.randint(1,10)
# for i in range(3):
#     wanjia = int(input('请输入一个整数'))
#     if wanjia == com:
#         print('猜对了')
#         break
#     elif wanjia>com:
#         print('猜大了')
#     elif wanjia<com:
#         print('猜小了')
# else:
#     print(f'很遗憾 你输了,com={com}')


# 153 输出 白位  十位  个位
# a = 153
# print(a // 100)
# print(a // 10 %10)   # a//10=15   a%10=5
# print(a % 10)   #取余为3

# for i in range(100,1000):
#     a = i //100
#     b = i //10%10
#     c = i % 10
#     if a**3+b**3+c**3==i:
#         print(i)

# a = int(input('请输入一个数字:   '))
# b=1
# c=0
# for j in range(1,a+1):
#     b*=j
#     c+=b
# print(c)

# i=0
# for a in range(1,6):
#     i+=a
# print(i)


# i = 1
# s = 0
# for a in range(1,6):
#     i*=a
#     print(f'i={i}',end='\t')
#     s+=i
#     print(f's={s}')
# print(s)