# _*_ conding : utf-8 _*_
# @Time : 2022/9/7 15:46
# @Author : LWQaQ
# @File : python27_get请求的quote的方法
# @Project : PycharmProjects

# 获取 https://www.baidu.com/s?tn=39042058_40_oem_dg&ie=utf-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6  的网页源码

import urllib.request
# 定义url路径   可以使用quote方法
url = 'https://www.baidu.com/s?wd='
# url = 'https://jable.tv/videos/stars-703/'
# 模拟网页访问
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
# 请求对象的定制化
herders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# 使用quote方法将中文转化为unicode编码的格式
name = urllib.parse.quote('周杰伦')
print(name)
url = url + name
print(url)
# 请对对象封装
request = urllib.request.Request(url=url, headers=herders)
# 发送请求
response = urllib.request.urlopen(request)
# 接收相应内容
content = response.read().decode('utf-8')
# 输入内容
print(content)
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-12: ordinal not in range(128)---------默认检索127，编码超出！---需要变成unicode编码