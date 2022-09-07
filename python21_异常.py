# @Time : 2022/9/5 17:08
# @Author :lwQaQ    
# @File : python21_异常
# @Project : python基础

# 读取一个没有文件的异常  io.UnsupportedOperation: not readable
try:
    fp = open('text001.txt', 'r')
    fp.read()
except FileNotFoundError:
    print('文件不存在')

# 异常的格式
# try:
#     可以能出现异常的代码
# except: 异常的类型
#     友好的提示
