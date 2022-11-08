'''
爬虫:模仿浏览器,根据自己指定的规则 获取所需要的数据
分类:统用爬虫 --- 针对全网进行爬取,百度，谷歌 ....
    聚焦爬虫 --- 只针对某个网站进行爬取
爬虫的流程:1.模仿浏览器,分析网址发送请求
         2.制定规则,获取资源
         3.保存获取到的资源
'''
import re
import requests
a = input('请输入查询的内容：   ')
url = f'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={a}'
# url=f'https://www.sogou.com/web?query={a}'
#请求头
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'}
#发送请求
r=requests.get(url,headers=headers)  #get发送请求的一种方式(常用)
# print(r)  #<Response [200]> 状态码 200表示响应成功
'''
读取响应
1.text 字符串的方式读取所有
2.content 以二进制的方式读取所有
'''
# r.encoding='utf-8'
# print(r.text)
# print(r.content.decode()) #默认utf-8

html = r.content.decode()
print(html)

#查看请求头
# print(r.request.headers)
# data = re.findall('<title>(.*)</title>',html)
# print(data)
# with open('baid.txt','w',encoding='utf-8')as f:
#     f.write(data[0])