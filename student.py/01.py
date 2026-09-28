# name="我是小明"
# salary=10000.5
# print(f"{name}的工资是{salary}")
# shuaige="方明杰"
# print(f"帅哥是{shuaige}")
# a=10
# b=20
# c=a * b
# print(f"a和b的和为{a+b}")
# print(f"a和b的乘积为{c}")
# # 定义变量存储商品名称“耳机”、价格199.9、库存50，格式化输出商品信息。
# goods_name="耳机"
# goods_price=199.9
# goods_stock=50
# print(f"商品名称是{goods_name}，价格是{goods_price}，库存是{goods_stock}")
# score=83
# if score>=90:
#     print("优秀")
# elif  score<=90 and score>=60:
#     print("中等")
# else:
#     print("不及格")
from os.path import split

# try:
#     age = int(input("请输入年龄："))
#     if age>=18:
#         print("已成年")
#     elif age<0:
#         print("输入的年龄格式不正确")
#     elif age>150:
#         print("输入的年龄格式不正确")
#     else:
#         print("未成年")
# except ValueError:
#     print("输入的年龄格式不正确")


# num=int(input("请输入一个数字："))
# if num>0:
#     print("是正数")
# elif num<0:
#     print("是负数")
# else:
#     print("是零")
# from collections.abc import Iterator
# list_demo = [1, 2, 3] # 可迭代对象
# iterator = iter(list_demo) # 等价于 list_demo.__iter__()
# # 判断对象是否是迭代器
# print(isinstance(iterator, Iterator)) # True
# while True:
#     try:
#          print(next(iterator)) # 等价于iterator.__next__()
#     except StopIteration:
#         break
# print(list_demo)

#批量管理多人员薪资数据 列表/循环
# list=[['张三',1999,8000],['李四',1998,7000],['王五',1997,6000],['赵六',1996,5000],['孙七',1995,4000],['周八',1994,3000]]
# for name in list:
#     print(str(name[2]),end="\t") # 打印列表中每个元素的第三个字符
# print("循环结束")
shuiguo=['苹果','香蕉','橙子']
for name in shuiguo:
    print(name)

num=[1,2,3,4,5]
for i in num:
    num1=i**2
    print(num1)

# 定义姓名列表 ["小明","小红","小李"]，使用循环输出“小明,小红,小李是我的同学”。
name=["小明","小红","小李"]
for i in name:
    print(f"{i}是我的同学")






