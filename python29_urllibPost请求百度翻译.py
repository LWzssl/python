# _*_ conding : utf-8 _*_
# @Time : 2022/9/7 17:47
# @Author : LWQaQ
# @File : python29_urllibPost请求百度翻译
# @Project : PycharmProjects
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

# 验证用户
herders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

# post请求的参数必须要进行编码
data = {
    'kw': 'super'
}
# data = urllib.parse.urlencode(data)
data = urllib.parse.urlencode(data).encode('utf-8')
print(data)

request = urllib.request.Request(url=url, data=data, headers=herders)
print(request)

# TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.data的数据类型不对
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(type(content))
print(content)
# 字符串转化为json对象

obj = json.loads(content)
print(obj)
# post请求方式的参数 必须编码  data = urllib.parse.urlencode(data).encode('utf-8')
# 编码之后必须调用encode方法
# 参数是放在请求对象定制的方法中  request = urllib.requset.Request()
