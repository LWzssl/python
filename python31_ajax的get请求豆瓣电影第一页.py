# _*_ conding : utf-8 _*_
# @Time : 2022/9/8 17:43
# @Author : LWQaQ
# @File : python31_ajax的get请求豆瓣电影第一页
# @Project : PycharmProjects

# get请求获取豆瓣电影第一页数据，保存起来

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

# 请求对象的定制

request = urllib.request.Request(url=url, headers=headers)


# 获取相应的数据

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

# 将数据下载到本地
# UnicodeEncodeError: 'gbk' codec can't encode character '\xf8' in position 1490: illegal multibyte sequence 有中文
# open 方法默认情况下使用的是gbk的编码，如果我们想要保存汉字，那么需要在open方法中指定编码的格式为 utf-8
# fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(content)
# fp.close()

# 另一种形式表示
with open('douban1.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
    fp.close()