# @Time : 2022/8/23 16:06
# @Author :lwQaQ    
# @File : python_列表高级
# @Project : python基础

# append 在列表的最后来添加一个对象或者数据
# food_list = ['宫爆鸡丁', '水煮肉片']
# print(food_list)
# food_list.append('小鸡炖蘑菇')
# print(food_list)

# insert 插入 [] list  index 插入数据的下表
# char_list = ['a', 'c']
# print(char_list)
# char_list.insert(1, 'b')
# print(char_list)
# char_list.insert(3, 'd')
# print(char_list)

# extend  合并两个字符串
# number = [1, 2, 3]
# number1 = [4, 5, 6]
# number.extend(number1)
# print(number)
# ------------------------------------------修改----------------------------------------------
# city_list = ['北京', '上海', '武汉', '西安', '广州']
# print(city_list)
# city_list[3] = '石家庄'
# print(city_list)
# -------------------------------------------查找-----------------------------------------------
# in not 存在或者不存在返回true或者false
# computer_list = ['cpu', '鼠标', '键盘']
# 判断控制台输入的数据是否在列表中存在 in
# isList = input("请输入你想要查询的计算机组件的列表")
# if isList in computer_list:
#     print("组件存在")
# else:
#     print("组件不存在，请重新查找")

# 判断控制台输入的数据是否在列表中存在 not in
# ball_list = ['篮球', '足球', '橄榄球']
# isList = input("请输入你想要查询的球类的列表")
# if isList not in ball_list:
#     print("球类不存在")
# else:
#     print("球类存在")
# --------------------------------------------删除元素----------------------------------------------
# 删除 del pop 最后一个元素  remove 根据元素的值进行删除
a_list = [1, 2, 3, 4, 5]
print(a_list)
# 根据下标删除列表中的元素
# del a_list[2]
# print(a_list)
# 删除列表的最后一个元素
# a_list.pop()
# print(a_list)
# 根据元素的值进行删除
a_list.remove(2)
print(a_list)