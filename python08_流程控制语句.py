# @Time : 2022/8/22 15:32
# @Author :lwQaQ
# @File : python_流程控制语句
# @Project : python基础

# if关键字(格式必须正确,否则会提示缩进错误)
#   if关键条件:
#     执行语句
# age = 19
# if age > 18:
#     print("你可以开车了")
#
# # if else 判断语句
# age = input("请输入你的年龄")
# # 进行数据类型转化
# if int(age) > 18:
#     print("你已经成年了")
#
# else:
#     print('未成年请注意安全')

# elif流程控制语句
#     在控制台上输出你的成绩,根据你的成绩判断你所在的区间
# score = float(input("请输出你的成绩"))

# 条件全部满足,以后内容都会输出.不符合要求.故而使用elif
# if score >= 90:
#     print("优秀")
# if score >= 80:
#     print("良好")
# if score >= 70:
#     print("中等")
# if score >= 60:
#     print("及格")
# if score < 60:
#     print("不及格")
# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("良好")
# elif score >= 70:
#     print("中等")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")

# for流程空值语句
# word = "China"
#
# for i in word:
#     print(i)
# for循环遍历range range方法的结果是一个可以遍历的对象 从0开始左闭右开区间
# for i in range(5):
#     print(i)
# 第一个是起始值，第二个是结束值
# for i in range(1, 6):
#     print(i)
# 第一个是起始值，第二个是结束值，第三个是步长
# for i in range(1, 10, 3):
#     print(i)

# 应用场景，爬虫过程中会爬取一个列表返回给我们，会爬取一个个的列表给我，需要对列表进行循环遍历输出
# 循环一个列表
a_list = ['卡卡罗特', '贝吉塔', '比克大魔王']
# 遍历列表中的元素
# for i in a_list:
#     print(i)
# 遍历列表中的下标
print(len(a_list))
for i in range(len(a_list)):
    print(i)