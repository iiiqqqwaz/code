#文本的方式读取 格式： 列表
# import csv
# with open('豆瓣2.csv','r')as f:
#     reader =csv.reader(f)   #创建以文本列表方式读取的对象
#     for i in reader:
#         print(i)

#以字典的方式读取
# import csv
# with open('豆瓣2.csv','r')as f:
#     reader=csv.DictReader(f) #创建以字典方式读取的对象
#     for i in reader:
#         # print(i['名称']) #用键索引值
#         print(i)          #获取键值对


#文本写入
# import csv
# header=['name','age','sex']
# values=[('xiaoming',18,'男'),('xiaohong',19,'nv')]
# with open('testA.csv','w',newline='')as f: #newline='' 避免空行
#     writer = csv.writer(f) #创建一个写入对象
#     writer.writerow(header)
#     writer.writerows(values)

#字典 键值对的方式写入
# import csv
# header=['name','age','sex']
# values=[{'name':'xiaoming','age':18,'sex':'男'},{'name':'xiaohong','age':19,'sex':'nv'}]
# with open('test1.csv','w',newline='')as f:
#     writer = csv.DictWriter(f,header)
#     writer.writeheader()
#     writer.writerows(values)