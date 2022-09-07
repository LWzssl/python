# @Time : 2022/9/5 16:41
# @Author :lwQaQ    
# @File : python20_文件的序列化和反序列化
# @Project : python基础

# 写入文件  默认情况只能把写入字符串到文件中
# fp = open('text.txt', 'w')
# fp.write('helloWorld')
# fp.close()

# 如何写入列表呢
# fp = open('text.txt', 'w')
# name_list = ["zhangsan", "lisi"]
# # TypeError: write() argument must be str, not list
# # 所以要进行序列化
# fp.write(name_list)
# fp.close()

# 序列化的两种方式

# dumps()
# fp = open('test.txt', 'w')
# name_list = ["zhangsan", "lisi"]
# print(type(name_list))
# # 将列表序列化
# # 导入json模块到该文件中 import json
# import json
# # 序列化 json.dumps
# world = json.dumps(name_list)
# print(type(world))
# fp.write(world)
# fp.close()

# dump()

# 将字符转化为字符串的同时，指定一个文件对象，可以直接将转化后的字符串写入目标文件中
# import json
# fp = open("test.txt", 'w')
# name_list = ["zhangsan11", "lisi"]
# json.dump(name_list,fp)
# fp.close()

# ---------------------------------------------------反序列化--------------------------------------

# 将json 字符串转化成python对象
import json
fp = open("test.txt", 'r')
# content = fp.read()
# print(content)
# print(type(content))
# #loads()
# name =json.loads(content)
# print(name)
# print(type(name))
#load()
name1 = json.load(fp)
print(name1)
print(type(name1))
fp.close()
