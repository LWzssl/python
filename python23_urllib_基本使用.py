import urllib.request
# @Time : 2022/9/5 18:14
# @Author :lwQaQ    
# @File : python23_urllib_基本使用
# @Project : python基础

# 使用urllib获取百度网页的源码

# (1)定义一个url 就是你要访问的地址

url = 'http://www.baidu.com'

# (2)模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# （3）获取响应的内容
# read 返回的是字节形式的二进制数据
# 将二进制的数据转化为字符串
# 进行解码操作 decode('编码的格式')
contents = response.read().decode('utf-8')
print(contents)