# _*_ conding : utf-8 _*_
# @Time : 2022/9/7 15:15
# @Author : LWQaQ
# @File : python26_urllib_请求对象的定制
# @Project : PycharmProjects
import urllib.request
url = 'https://www.baidu.com'


# http/https 协议类型   www.baidu.com  主机    80/443 段端口   s 路径     参数  锚点


# 使用UA 进行反爬虫操作
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36   字典类型的数据不能进行直接使用

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# 不可以直接使用，需要传入字符串或者object,进行请求对象的定制
# request = urllib.request.Request(url, header)
#                   def __init__(self, url, data=None, headers={},
#                  origin_req_host=None, unverifiable=False,
#                  method=None):
# 需要加入变量的指定名字----关键字传参
request = urllib.request.Request(url=url, headers=header)
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)