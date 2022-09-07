# @Time : 2022/8/23 17:46
# @Author :lwQaQ    
# @File : python_切片
# @Project : python基础


s = "hello world"
# 在切片中直接写一个下标
print(s[4])

# 遵循左闭又开区间
print(s[0:4])

# 只有起始的没有终止的 从起始的开始一直到末尾
print(s[1:])

# 从下标为0的元素开始，一直到末尾规定的位置
print(s[:4])

# 从下标为0的开始到6结束，每次2个步长
print(s[0:6:2])
