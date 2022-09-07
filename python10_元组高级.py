# @Time : 2022/8/23 16:45
# @Author :lwQaQ    
# @File : python_元组高级
# @Project : python基础


# 元组和列表的区别： 元组的数据不能修改  元组是（）
a_tuple = (1, 2, 3)
print(a_tuple)
print(a_tuple[0])

# 实列  TypeError: 'tuple' object does not support item assignment
# a_tuple[1] = 3
# print(a_tuple)
# 定义只有一个元素的元组，要在元素后边加一个，
# b_tuple = (1)
# print(type(b_tuple))
b_tuple = (1,)
print(type(b_tuple))