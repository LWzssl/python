# _*_ conding : utf-8 _*_
# @Time : 2022/9/8 17:56
# @Author : LWQaQ
# @File : python32_aiax的get请求豆瓣前十页的数据
# @Project : PycharmProjects

# 下载豆瓣电影前十页的数据 （page-1）*20

# 请求对象的定制
# 获取响应的数据
# 下载数据
import urllib.parse
import urllib.request


#Request URL: https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20
def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    data = {
        'start': (page - 1) * 20,
        "limit": 20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request



# 封装获取响应数据
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
    return content



def down_load(page, content):
    with open('douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)

# 程序的入口
if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页码'))

    for page in range(start_page, end_page + 1):
        #  每一页都有自己的请求对象定制
        request = create_request(page)
        print(request)
        # 获取响应数据
        content = get_content(request)

        # 下载数据
        down_load(page, content)
