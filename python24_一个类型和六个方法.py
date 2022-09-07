# _*_ conding : utf-8 _*_
# @Time : 2022/9/7 14:32
# @Author : LWQaQ
# @File : python24_一个类型和六个方法
# @Project : PycharmProjects

import urllib.request

# (1) 定义要访问的url
url = 'http://www.baidu.com'

# (2) 模拟浏览器进行数据发送
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response的类型---<class 'http.client.HTTPResponse'>
# print(type(response))

# 按照一个字节一个字节的去读
# content = response.read()
# print(content)

# 代表返回多少个字节
# content = response.read(5)
# print(content)

# 按照行进行读取
# content = response.readline()
# print(content)

# 一行一行的去读取直到读取完成----还是二进制字节----可以通过解码进行变换decode('utf-8')
# content = response.readlines()
# print(content)

# 返回状态码 如果是200证明咱们自己的逻辑没有错
print(response.getcode())
# 返回url地址
print(response.geturl())
# 返回头部---状态信息--响应头
print(response.getheaders())
# 一个类型  HTTPResponse 六个方法  read() readline() readlines() getCode() geturl() getheaders()
