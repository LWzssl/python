# @Time : 2022/8/26 16:23
# @Author :lwQaQ    
# @File : python_字典高级
# @Project : python基础



# -------------------------------------------------查询------------------------------------------------------
# 定义一个字典
# person = {"name": '吴亦凡', "age": '28'}
# print(person["name"])
# print(person["age"])
# 使用字段中不存在的key   使用[]的方式获取字典中不存在的key的时候会发生异常,异常:KeyError: 'address'
# print(person["address"])
# print(person.get("name"))
# print(person.get("age"))
# 使用.get的方式获取字典中不存在的key的时候不会发生异常,会输出啊None
# print(person.get("address"))

# --------------------------------------------------修改--------------------------------------------------------
# 定义一个字典
# person = {"name": '张三', "age": '18'}
# print(person.get("name"), person.get("age"))
# 修改name的值
# person["name"] = "法外狂徒"
# print(person.get("name"))

# # --------------------------------------------------添加--------------------------------------------------------
# # 定义一个字典
# person = {"name": '张三', "age": '18'}
# print(person)
# # 添加一个新的key-value   如果键不存在,则新增;如果存在,则会变成修改这个元素
# person["address"] = "比尔吉沃尔"
# print(person)

# --------------------------------------------------删除--------------------------------------------------------
# # 定义一个字典
# person = {"name": '张三', "age": '18'}
# print(person)
# # 添加一个新的key-value   如果键不存在,则新增;如果存在,则会变成修改这个元素
# person["address"] = "比尔吉沃尔"
# print(person)
#
# # 删除字典的内容   del---针对指定元素删除;删除整个字典         clear--清空字典,保留字典对象
# del person["age"]
# print(person)
#
# # 删除全部
# # del person
#
# # 清空
# person.clear()
# print(person)


# --------------------------------------------------遍历--------------------------------------------------------
# # 定义一个字典
person = {"name": '张三', "age": '18', 'address': "伊拉克"}

# 遍历字典的key
for key in person.keys():
    print(key)

# 遍历字典的value
for value in person.values():
    print(value)
# 遍历字典的key 和 value
for key, value in person.items():
    print(key, value)

# 遍历字典的项(元素 以 , 分割的)
for item in person.items():
    print(item)
