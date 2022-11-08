import pymysql
#连接数据库
conn = pymysql.connect(host='192.168.2.124',
                       port=3306,
                       user='root',     #链接数据库的用户名
                       passwd='123456',#链接数据库的密码
                       charset='utf8')
#创建游标控制器
abc = conn.cursor()
#执行sql语句
abc.execute('show databases;') #查看具有哪些库
#1)接收上一行sql语句产生的结果,元组格式
# print(abc.fetchall())
#2)默认接收第一行 写入几 输出几接收几行内容
# print(abc.fetchmany())
#3)每次接收一行 本身具有累加功能
# print(abc.fetchone())

# abc.execute('create database ku2;')
# abc.execute('show databases;')
# print(abc.fetchall())

abc.execute('use ku2')
# abc.execute('create table biao1(name char(255),age char(255),sex char(255));')
abc.execute('show tables')
print(abc.fetchall())

abc.execute('insert into biao1 values("小明","十八","男");')
conn.commit() #提交
abc.execute('select * from biao1')
print(abc.fetchall())
#断开数据库
conn.close()