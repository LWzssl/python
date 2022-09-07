# _*_ conding : utf-8 _*_
# @Time : 2022/9/7 14:46
# @Author : LWQaQ
# @File : python25_urllib_下载
# @Project : PycharmProjects
import urllib.request

# 下载一个网页
# url_page = 'http://www.baidu.com'
#
# urllib.request.urlretrieve(url_page, 'baidu.html')
# # 下载一个图片
# url_image = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_bt%2F0%2F14090099665%2F1000.jpg&refer=http%3A%2F%2Finews.gtimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665125563&t=ab3c4bd39d87b27f9c45b15722bc9c21'
# urllib.request.urlretrieve(url_image,'liuhaocun.jpg')
# 下载一个视频
url_vide ='https://jable.tv/videos/stars-703/'
urllib.request.urlretrieve(url_vide, '视频下载.mp4')
