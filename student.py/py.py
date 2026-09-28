
# '''#开发购物车管理系统，实现商品的添加、删除、修改和查询功能。
# shopping_cart = {}
# '''
# ######






# '''
# print("欢迎使用购物车管理系统")
# while True:
#     print("1. 添加商品")
#     print("2. 删除商品")
#     print("3. 修改商品")
#     print("4. 查询商品")
#     print("5. 显示购物车")
#     print("0. 退出系统")
#     choice = input("请输入操作编号：")
#     match choice:
#         case "1":
#             Name = input("请输入商品名称：")
#             price = float(input("请输入商品价格："))
#             num = int(input("请输入商品数量："))
#             if Name in shopping_cart:
#                 shopping_cart[Name]['num'] += num
#                 shopping_cart[Name]['price'] = price
#                 print("商品已在购物车中，数量已更新。")
#             else:
#                 shopping_cart[Name] = {'price': price, 'num': num}
#         case "2":
#             Name = input("请输入要删除的商品名称：")
#             if Name in shopping_cart:
#                 del shopping_cart[Name]
#                 print("商品已从购物车中删除。")
#             else:
#                 print("商品不在购物车中。")
#         case "3":
#             Name = input("请输入要修改的商品名称：")
#             if Name not in shopping_cart:
#                 print("商品不在购物车中。")
#                 continue
#             num = int(input("请输入新的商品数量："))
#             price = float(input("请输入新的商品价格："))
#             shopping_cart[Name] = {'price': price, 'num': num}
#             print("商品信息已更新。")
#         case "4":
#             Name = input("请输入要查询的商品名称：")
#             if Name in shopping_cart:
#                 print(f"商品名称：{Name}")
#                 print(f"商品价格：{shopping_cart[Name]['price']}")
#                 print(f"商品数量：{shopping_cart[Name]['num']}")
#             else:
#                 print("商品不在购物车中。")
#         case "5":
#             print("购物车中的商品如下：")
#             if not shopping_cart:
#                 print("购物车为空。")
#             for Name, info in shopping_cart.items():
#                 print(f"商品名称：{Name}")
#                 print(f"商品价格：{info['price']}")
#                 print(f"商品数量：{info['num']}")
#         case "0":
#             print("退出系统，欢迎下次使用。")
#             break
#         case _:
#             print("输入错误，请重新输入！")'''

# '''
# ## 题1：生成器

# 使用生成器表达式创建一个生成器，生成 1 到 10 的偶数。然后使用for循环遍历该生成器，打印每个偶数。
# '''

# # gen = (i for i in range(1, 11) if i % 2 == 0)
# #
# # for i in gen:
# #     print(i)
# '''## 题2：迭代器

# 创建一个迭代器类MyIterator，实现__iter__和__next__方法。该迭代器可以遍历任意序列的元素，且步长是2。'''
# class MyIterator:
#     def __init__(self, data):      # 参数改为 data，接收任意序列
#         self.data = data
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.data):   # 用序列长度判断边界
#             result = self.data[self.index]  # 返回序列元素，不是索引
#             self.index += 2                 # 步长改为 2
#             return result
#         else:
#             raise StopIteration

# rev = MyIterator([1, 2, 3, 4, 5])
# for i in rev:
#     print(i)
# '使用生成器表达式创建一个生成器，生成 1 到 10 的偶数。然后使用for循环遍历该生成器，打印每个偶数'
# gen = (i for i in range(1, 11) if i % 2 == 0)
# for i in gen:
#     print(i)

# # 一、编程题目（15 道）
# # 编写程序，创建列表lst = [12,45,7,89,23]，完成：输出列表长度、最大值、最小值、所有元素求和。
# lst = [12,45,7,89,23]
# print("列表长度:", len(lst))
# print("最大值:", max(lst))
# print("最小值:", min(lst))
# print("所有元素求和:", sum(lst))
# # 给定列表 names = ["张三","李四","王五"]，使用 append 追加 “赵六”，使用 insert 在索引 1 位置插入 “钱七”，最后打印最终列表。
# names = ["张三","李四","王五"]
# names.append("赵六")
# names.insert(1, "钱七")
# print("最终列表:", names)
# # 现有列表 data = [10,20,30,40,50]，利用切片实现列表逆序输出（不要使用 reverse 方法）。
# data = [10,20,30,40,50]
# print("逆序输出:", data[: :-1])
# # 使用列表推导式生成 1~20 之间所有偶数组成的列表并打印。
# list_even = [i for i in range(1, 21) if i % 2 == 0]
# print("1~20之间的偶数列表:", list_even)
# # 给定字符串 s = "hello python"，完成： 1）全部转为大写； 2）按空格分割成列表； 3）统计字符o出现次数。
# s = "hello python"
# print("全部转为大写:", s.upper())
# print("按空格分割成列表:", s.split())
# print("字符o出现次数:", s.count('o'))
# # 接收字符串 s = " abc123 "，去除字符串两边空格，判断处理后的字符串是否全部由字母组成，输出判断结果。
# s = " abc123 "
# s_stripped = s.strip()
# print("去除两边空格后的字符串:", s_stripped)
# print("是否全部由字母组成:", s_stripped.isalpha())

# # 定义元组t = (11,22,33,44,55)，通过切片获取中间 3 个元素；尝试使用元组解包，把第一个元素给变量a，剩下全部元素给列表rest并打印。
# t = (11,22,33,44,55)
# middle_three = t[1:4]
# print("中间3个元素:", middle_three)
# a, *rest = t
# print("第一个元素a:", a)
# print("剩下的元素列表rest:", rest)
# # 给定两个列表list_a = [2,3,5,5,7]，list_b = [5,7,9,11]，借助集合求出两个列表的交集，并打印结果。
# list_a = [2,3,5,5,7]
# list_b = [5,7,9,11]
# intersection = set(list_a) & set(list_b)
# print("两个列表的交集:", list(intersection))

# # 集合去重：给定列表nums = [1,2,2,3,3,3,4,4,5]，利用集合对列表去重，再转回列表打印输出。
# nums = [1,2,2,3,3,3,4,4,5]
# unique_nums = list(set(nums))
# print("去重后的列表:", unique_nums)

# # 创建字典student = {"name":"小明","age":16,"gender":"男"}， 1）使用 get 获取name的值； 2）获取不存在 key 为score，设置默认值为 0； 3）新增键值对score:90，打印字典。
# student = {"name":"小明","age":16,"gender":"男"}
# print(student.get("name"))
# print(student.get("score",0))
# student["score"]=90
# print(student)
# # 遍历字典info = {"a":10,"b":20,"c":30}，分别遍历打印所有 key、所有 value、所有 key‑value 键值对。
# info = {"a":10,"b":20,"c":30}
# for key in info:
#     print(key)
# for value in info.values():
#     print(value)
# for key,value in info.items():
#     print(key,value)
# # 编写无参函数print_hello()，函数内部循环打印 1‑10 数字，调用该函数执行。
# def print_list():
#     for item in range(1,11):
#         print(item)
# print_list()
# # 编写带参数函数calc_square(num)，接收 1 个数字参数，返回该数字的平方；调用函数计算 12 的平方并打印返回结果。
# def calc_square(num):
#     # num=int(input('请输入数字'))
#     num1=num**2
#     print(num1)
#     return num1
# calc_square(12)
# # 定义函数sum_all(*args)，使用可变位置参数*args，函数内部计算所有传入数字的总和并返回；调用：sum_all(1,2,3,4,5)输出总和。
# def sum_all(*args):
#     total=0
#     for num in args:
#         total+=num
#     print(total)
#     return total
# sum_all(1,2,3,4,5)
# # 定义函数show_user(name, age, **kwargs)，位置参数接收姓名、年龄，可变关键字参数接收其他信息；调用时传入：name=”小红”，age=17，city=”广州”，hobby=”看书”，函数内部打印全部参数。
# def show_user(name, age, **kwargs):
#     print(name)
#     print(age)
#     print(kwargs)
# show_user(name='小红',age=17,city='广州',hobby='看书')
# # 二、面试简单题（5 道）
# # 说一说列表list和元组tuple的区别？什么是可变与不可变类型？
# 列表可变，元组不可变。列表可以修改其内容（添加、删除、修改元素），可变 指的是对象创建后，其内容可以被原地修改（增删改元素），而不改变对象的内存地址。不可变 指的是对象创建后，其内容不能被修改，任何"修改"操作实际上都会创建一个新对象。
# # 集合 set 有什么特点？一般什么场景会使用集合？
# set 是无序的、不可重复的元素集合。特点包括：1）元素唯一性；2）无序性；3）支持集合运算（交集、并集、差集等）。一般用于去重、快速查找、数学集合运算等场景。
# # 字典的 key 有什么要求？哪些类型可以作为字典 key，哪些不可以？
# 字典的 key 必须是不可变类型（如字符串、数字、元组等），且唯一。可作为字典 key 的类型包括：字符串、数字、元组（只要元组中的元素也是不可变类型）。不可以作为字典 key 的类型包括：列表、字典、集合等可变类型。
# # 简述append()、extend()、insert()三个列表方法的区别。
# append()：在列表末尾添加一个元素，参数可以是任意类型，包括列表本身。
# extend()：在列表末尾一次性追加另一个可迭代对象的所有元素。
# insert()：在指定位置插入一个元素，原有元素向后移动。
# # 函数中*args和**kwargs分别是什么作用？
# *args用于接收任意数量的位置参数，函数内部将其作为一个元组处理。**kwargs用于接收任意数量的关键字参数，函数内部将其作为一个字典处理。




# from functools import reduce
# import heapq

# list_demo = [5, 2, 9, 1, 7, 6, 3, 8, 4]
# print("最小的3个奇数：", heapq.nsmallest(3, list_demo, key=lambda x: x if x % 2 != 0 else float('inf')))

# print("最大的3个偶数：", heapq.nlargest(3, list_demo, key=lambda x: x if x % 2 == 0 else float('-inf')))
# print("排序后的列表：", sorted(list_demo))





# student_list = [{"name": "zhang3", "age": 36}, {"name": "li4", "age": 14}, {"name": "wang5", "age": 25}]
# student_list = sorted(student_list, key=lambda s: s["age"])
# print("按照年龄排序：", student_list)
# filter_result = filter(lambda s: s["age"] > 18, student_list)
# print("18岁以上的：", list(filter_result))
# map_result = map(lambda s: s["name"], student_list)
# print("姓名：", list(map_result))
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
# # 统计列表中所有人的年龄总和
# # print(reduce(lambda p1, p2: p1["age"] + p2["age"], person_list)) # 这里报错 因为年龄相加之后 无法直接赋值给某个字典对象
# person_list = [
# {"name":"jack","age":21,"address":"深圳"},
# {"name":"jeery","age":11,"address":"深圳"},
# {"name":"tom","age":35,"address":"广州"},
# {"name":"john","age":25,"address":"广州"},
# {"name":"lily","age":55,"address":"东莞"}
# ]

# print(reduce(lambda total_age, p: p["age"] + total_age, person_list,0))

# print("按地址分组统计年龄总和：", reduce(lambda total_age, p: {**total_age, p["address"]: total_age.get(p["address"], 0) + p["age"]}, person_list, {}))
# print("按地址分组统计人数：", reduce(lambda total_count, p: {**total_count, p["address"]: total_count.get(p["address"], 0) + 1}, person_list, {}))


# x=1

# def nogal ():
#     a=9
#     global x
#     x=5
#     print(x)
#     def inner():
#         nonlocal a
#         a=10
#         print(a)
#     inner()
# nogal()
# # 综合题6（不定长参数+map/filter/reduce综合）
# # 需求
# # 定义不定长参数函数，接收任意多个数字；
# # 使用filter过滤出所有正数；
# # 使用map将每个正数乘以2；
# # 使用reduce对处理后的数字求和并返回结果； (自行查阅reduce用法)
# # 调用函数传入参数-5, 8, -2, 10, 3，打印最终总和。 要求：导入functools.reduce，全程搭配lambda匿名函数实现

# def process_numbers(*args):
#     positive_numbers = filter(lambda x: x > 0, args)
#     doubled_numbers = map(lambda x: x * 2, positive_numbers)
#     total_sum = reduce(lambda x, y: x + y, doubled_numbers, 0)
#     return total_sum

# print(process_numbers(-5, 8, -2, 10, 3))
# 定义父类
class Animal:

    def __init__(self, name, **kwargs):
        print("Animal父类构造方法")
        self.name=name
        super().__init__(**kwargs)
# 定义父类
class Fish(Animal):

    def __init__(self, name=None, **kwargs):
        print("Fish父类构造方法")
        super().__init__(name,**kwargs) # 传递剩余参数
# 定义父类
class Person(Animal):

    def __init__(self, name=None, gender=None, **kwargs):
        print("Person父类构造方法")
        self.gender = gender
        super().__init__(name,**kwargs) # 传递剩余参数

# 定义子类
class RoboticFish(Fish, Person):

    def __init__(self, name, gender, power_capacity):
        print("RoboticFish子类构造方法")
        self.power_capacity = power_capacity
        super().__init__(name=name, gender=gender)
    def __str__(self):
        return f"鱼形机器人名字：{self.name}，性别：{self.gender}，电量：{self.power_capacity}"
# 测试
# 查看方法解析顺序MRO
print(RoboticFish.__mro__)
r = RoboticFish("落雁", "女",98)
print(r)


# 定义Account类
class Account:
    def __init__(self, balance):
        self.__balance = balance
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("取款金额不能为负数")
        if amount > self.__balance:
            raise ValueError("余额不足")
        self.__balance -= amount
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("存款金额不能为负数")
        self.__balance += amount
    @property
    def balance(self):
        return self.__balance
# 测试
account = Account(1000)
try:
    account.withdraw(-500)
except ValueError as e:
    print("取款失败，", e)
try:
    account.deposit(-500)
except ValueError as e:
    print("存款失败，", e)
try:
    account.withdraw(1500)
except ValueError as e:
    print("取款失败，", e)
try:
    account.withdraw(500)
    print("取款成功，余额为：", account.balance)
except ValueError as e:
    print("取款失败，", e)




# 定义计算三角形面积的函数
def calculate_triangle_area(a, b, c):
    """计算三角形面积的函数"""
    if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
        raise ValueError("输入的数字无法构成三角形")
# 使用海伦公式计算面积
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area
# 处理三角形的函数
def process_triangle():
    """处理三角形的函数"""
    try:
        a = int(input("请输入边长a的值："))
        b = int(input("请输入边长b的值："))
        c = int(input("请输入边长c的值："))
# 调用计算面积函数
        area = calculate_triangle_area(a, b, c)
        print(f"三角形的面积为：{area}")
    except ValueError:
        print("输入错误，请重新输入")
        raise # 重新抛出异常给上层
# 测试代码
while True:
    try:
        process_triangle()
        break
    except ValueError as e:
        print(e)



"""
自定义异常
"""
# 定义异常类
class NotATriangleError(Exception):
    """自定义异常类"""
pass
# 测试


while True:
    try:
        a=int(input("请输入第一个数字"))
        b=int(input("请输入第二个数字"))
        c=int(input("请输入第三个数字"))
        if a + b <= c or a + c <= b or b + c <= a or a<=0 or b<=0 or c<=0:
            raise NotATriangleError("输入的数字无法构成三角形")
        print("三角形的周长为：", a + b + c)
        break
    except ValueError as e:
        print("输入的数字不合法",e)
    except NotATriangleError as e:
        print(e)


