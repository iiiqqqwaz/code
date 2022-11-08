'''
xlrd    --- 读取
xlwt    --- 写入
xlutils --- 追加
'''

#写入
# import xlwt
# f = xlwt.Workbook()          #打开一个excel表格
# sheet = f.add_sheet('信息表') #添加一个标签页,括号写的是标签页名字
# sheet.write(0,1,'小明')       #给标签页加入数据,括号里写的是行列内容
# f.save('软件测试.xls')          #保存


#读取
# import xlrd
# f = xlrd.open_workbook('软件测试.xls')  #打开要读取的excel表格
# print(f.nsheets)                       #获取表格中有多少标签页
# print(f.sheet_names())                #获取表格中标签页的名字
# sheet=f.sheets()[0]         #根据索引获取到想要操作的标签页
# sheet1=f.sheet_by_name('信息表') #根据名字获取想要操作的标签页
# 翻译为 sheet:表 by:的 name:名字

# print(sheet.nrows)      #获取标签页中有多少行内容
# print(sheet.row_values(1)) #根据索引获取标签页某一行的内容
# for i in range(sheet.nrows):    #循环行数
#     print(sheet.row_values(i))  #打印每一行的内容

# print(sheet.ncols)    #获取标签页中有多少列内容
# print(sheet.col_values(0)) #根据索引获取某一列内容
# for j in range(sheet.ncols):      #循环列数
#     print(sheet.col_values(j))    #打印每一列的内容

# print(sheet.cell(0,1).value)  #根据索引 获取某个单元格的内容


#追加
# import xlrd
# from xlutils.copy import copy
# f = xlrd.open_workbook('软件测试.xls') #打开要操作的excel表格

# new_f = copy(f)                      #将xlrd对象拷贝转化为xlwt对象
# sheet = new_f.get_sheet(0)          #根据索引获取索要的标签页
# sheet.write(1,1,'tom')         #有数据的格子追加 覆盖原有内容
# new_f.save('软件测试.xls')


# sheet1 =f.sheet_by_name('信息表')
# print(sheet1.nrows)                 #读取有几行操作