# @Time : 2022/9/5 15:48
# @Author :lwQaQ    
# @File : python_局部变量和全局变量
# @Project : python基础

# 在函数的内部，定义的变量是局部变量，其作用的范围是函数的内部，函数的外部是不可以使用的

def f1():
    a = 1
    print(a)


f1()

a = 2

print(a)
