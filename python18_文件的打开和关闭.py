# @Time : 2022/9/5 16:03
# @Author :lwQaQ    
# @File : python_文件的打开和关闭
# @Project : python基础

# 创建一个文件.txt
# open 文件的路径  文件的模式 w：可写  r：可读
# open('text.txt', 'w')

# 打开一个存在的文件,并且写入
fp = open('text.txt', 'w')
fp.write('helloWorld')
# 文件的关闭
fp.close()