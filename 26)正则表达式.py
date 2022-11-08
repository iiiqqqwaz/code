'''
re --- 正则表达式模块(列表格式)
格式:re.findall(正则条件,需要匹配的字符串)
贪婪模式:从第一个符合条件的开始到最后一个符合条件的结束 尽可能多的去匹配
非贪婪模式(?):从第一个符合条件的开始到下一个符合条件的结束 尽可能少的去匹配
re.S ---可以匹配包括换行符在内的任意字符
re.I --- 不区分大小写
sub()
'''
import re
# a='abcda'
# b=re.findall('a.*a',a)
# print(b)  #['abcda']

'''从第一个a开始最后一个a结束,带括号就是匹配括号里面的内容'''
#贪婪模式
# a='abcda'
# b=re.findall('a(.*)a',a)
# print(b)    #['bcd']

# a='adsdasda'
# b=re.findall('a(.*)a',a)
# print(b)    #['dasdasda']


#非贪婪模式
# a='adsdasda'
# b=re.findall('a(.*?)a',a)
# print(b)    #['dsd']

# a='adsadasda'
# b=re.findall('a(.*?)a',a)
# print(b)    #['ds', 'sd']

# a='abcdasdafgawsdga'
# b=re.findall('a(.*?)a',a)
# print(b)    #['bcd', 'fg']

# a='ab\ncdasdafgawsdga'
# b=re.findall('a(.*?)a',a,re.S)
# print(b)      #['b\ncd', 'fg']

# a='Abcdasdafgawsdga'
# b=re.findall('a(.*?)a',a)
# print(b)        #['sd', 'wsdg']

# a='Abcdasdafgawsdga'
# b=re.findall('a(.*?)a',a,re.I)
# print(b)       #['bcd', 'fg']

#sub() --- 正则替换
# c = '123qwert'
# print(c.replace('123','aaa'))
# print(re.sub('123','aaa',c))

# c = '1qw2er3t'
# print(re.sub('[0-9]','aaa',c))