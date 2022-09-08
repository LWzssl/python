# _*_ conding : utf-8 _*_
# @Time : 2022/9/7 17:24
# @Author : LWQaQ
# @File : python28_urllib_get请求的urlincode方法
# @Project : PycharmProjects

# urlencode 多个参数的时候  必须已字典的形式存在
# https://www.baidu.com/s?sex='男'&wd=‘周杰伦’
import urllib.parse
# data = {
#     'wd': '周杰伦',
#     'sex': '男'
# }
#
# a = urllib.parse.urlencode(data)
# print(a)
import urllib.request

# 定义url路径   可以使用quote方法
base_url = 'https://www.baidu.com/s?'
# 定义拼接字符串
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}
data = urllib.parse.urlencode(data)
# 模拟网页访问
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
# 请求对象的定制化
herders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

url = base_url + data

# 请对对象封装
request = urllib.request.Request(url=url, headers=herders)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
