# @Time : 2022/8/22 15:12
# @Author :lwQaQ    
# @File : python_逻辑运算符性能优化
# @Project : python基础

# 当and的前边结果是false的时候，那么后边的代码就不会执行了
a = 36
a < 10 and print("会执行后边吗？，答案是不会")

a = 40

# or只要有一方为true的时候，结果就为true
a > 41 or print("这个会执行吗，答案是会的")
a > 39 or print("这个会执行吗，答案是不会")

# 格式化输出
age = 18
name = "两墨水"
print("我的年龄是%d，我的姓名是%s" % (age, name))

# 输出

password = input("请输入你的银行卡密码")

print("我的密码是:%s"% password)