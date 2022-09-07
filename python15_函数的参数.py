# @Time : 2022/9/5 15:19
# @Author :lwQaQ
# @File : python_函数的参数
# @Project : python基础

def sum():
    a = 1
    b = 2
    c = a + b
    print(c)


sum()


# ---------------------------------使用参数实现-------------------------------
def sum1(a, b):
    c = a + b
    print(c)

# 位置参数  按照位置一一对应的关系来传递参数
sum1(3, 4)

# 关键字传参 不推荐，会爆红
sum1(b = 2, a = 1)
