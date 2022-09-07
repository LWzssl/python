# @Time : 2022/8/23 14:44
# @Author :lwQaQ    
# @File : python_字符串高级
# @Project : python基础


# len 获取字符串的长度
word = 'woaininiaiwo'
print(len(word))

# find 查找指定内容在字符串中是否存在，如果存在，则返回第一次出现的索引值
index = word.find('w')
print(index)

# startWith endWith 以xxx开头 以XXX结尾
print(word.startswith('w'))
print(word.startswith('x'))
print(word.endswith('o'))
print(word.endswith('x'))

# count 统计某些字符出现的次数
print(word.count('w'))

# replace 字符串替换
print(word.replace('w', 'n'))

# split 切割字符串
number = '1#2#3#4'
print(number.split('#'))

# 大小写转换
print(word.upper())
print(word.lower())

# 去除字符串的空格

word1 = '    a    '
print(len(word1))
print(len(word1.strip(' ')))

# join 字符串拼接
# word2 = "hello"
# print(word2.join('a'))
word2 = "a"
print(word2.join("hello"))
