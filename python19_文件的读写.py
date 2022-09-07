# @Time : 2022/9/5 16:16
# @Author :lwQaQ    
# @File : python_文件的读写
# @Project : python基础


# 写数据 write

# fp = open('test1.txt', 'w')
# fp.write('hello World, I am here\n' * 5)
# fp.close()

# 如果文件存在，会先清空原来的数据，然后在写。如何追加呢？w--->a
# fp = open('test1.txt', 'a')
# fp.write('hello World, I am here\n' * 5)
# fp.close()

# 读数据

fp = open('test1.txt', 'r')
# 默认情况是一个字节一个字节的读，效率比较底下。修改成一行一行的读
# content = fp.read()
# 只能读取一行
# content = fp.readline()
# 读取多行，返回的是列表
content = fp.readlines()
for name in content:
    print(name)
print(content)

