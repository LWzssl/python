# @Time : 2022/9/5 15:31
# @Author :lwQaQ
# @File : python_函数的返回值
# @Project : python基础

# return 是返回的关键字，存在函数当中
def buyIceCream():
    return '冰淇淋'


# 如果有返回值，要使用变量来接受返回值
food = buyIceCream()
print(food)


# 案例练习 定义一个函数，计算两个值，并且返回计算的结果

def sumAndReturn(a, b):
    c = a - b
    return c


result = sumAndReturn(100, 50)
print(result)
