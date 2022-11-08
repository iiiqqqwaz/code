#字典推导式
#字典:字典key是1-5数字,values是key的二次方
#1.
# a={}
# for i in range(1,6):
#     a[i]=i**2
# print(a)

#2.
# a={i:i**2 for i in range(1,6)}
# print(a)


#将两个列表合并为一个字典
# a=['name','age','gender']
# b=['tom',20,'man']
# dict={a[i]:b[i] for i in range(len(a))}
# print(dict)



#提取上述电脑数量大于等于200字典的数据
#1.
# abc={'hp':256,'dell':156,'acer':234}
# a={}
# for i,j in abc.items():
#     if j >=200:
#         a[i] = j
# print(a)

#2.
# abc={'hp':256,'dell':156,'acer':234}
# b={i:j for i,j in abc.items() if j>=200}
# print(b)
