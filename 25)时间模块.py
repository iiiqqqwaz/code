'''结构-格式
格式-结构
结构-时间戳'''
import time
#时间戳
# print(time.time()) #现在的时间戳

#查看当前的时间 元组的形式  年月日 时分秒 wday=0 一星期中的第一天为0 yday一年的第几天
# print(time.localtime()) #以元组形式获取当前时间,()括号里面可以加时间戳 单位为秒
# time.struct_time(tm_year=2022, tm_mon=9, tm_mday=5, tm_hour=17, tm_min=7, tm_sec=52, tm_wday=0, tm_yday=248, tm_isdst=0)

#把元组类型的时间转换成现代化时间显示
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
#2022-09-05 17:08:24

#把现代化时间转化为元组类型的时间
# print(time.strptime('2022-09-05 15:22:06','%Y-%m-%d %H:%M:%S'))
# time.struct_time(tm_year=2022, tm_mon=9, tm_mday=5, tm_hour=15, tm_min=22, tm_sec=6, tm_wday=0, tm_yday=248, tm_isdst=-1)

# 把元组类型的时间转换为时间戳
# print(time.mktime(time.localtime()))
#1662368944.0

#等待(等待括号里面的时间停止,单位秒)
# time.sleep(5)

# '''输出前一天
# 输入2022-9-5
# 输出2022-9-4'''
# t1 = input('输入一个时间：  ')  # 格式
# t2 = time.strptime(t1, '%Y-%m-%d')  # 格式 转 结构
# t3 = time.mktime(t2)  # 结构 转 时间戳
# t4 = t3 - 86400  # 时间戳 计算前一天
# t5 = time.localtime(t4)  # 时间戳 转 结构
# t6 = time.strftime('%Y-%m-%d', t5)  # 结构 转 格式
# print(t6)  # 输出

