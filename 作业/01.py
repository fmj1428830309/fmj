# real_name="小王"
# age=22
#
# print(f"我叫{real_name}，今年{age}岁，每月税后薪资{month_salary}元")
# month_salary=6200.0
# if month_salary>=10000:
#     print("薪资等级：高")
# elif month_salary<10000 and month_salary>=5000:
#     print("输出薪资等级：中")
# elif month_salary<5000 and month_salary>0:
#     print("输出薪资等级：低")
# else:
#     print("输入有误")
#
#
# socre=int(input("请输入成绩"))
# if socre>=80:
#     print("优秀")
# elif socre<80 and socre>=60:
#     print("中")
# elif socre<60 and socre>0:
#     print("低")
# else:
#     print("输入有误")
#
# hobby_list = ["跑步","看书","打游戏"]
# for i in hobby_list:
#     print(f"我的爱好：{i}")
#
# for i in range(len(hobby_list)):
#     print(f"我的爱好：{hobby_list[i]}")
#     print(f"我的爱好：{hobby_list[i]}")
# nums=[3,5,7,9]
# for num in nums:
#     i=num**2
#     print(f"数字{num}的平方根是{i}")
#
# staff_list = [
#     ["小张",24,4800.0],
#     ["阿美",26,11000.0],
#     ["阿强",21,3500.0]
# ]
#
# for staff in  staff_list:
#     name = staff[0]
#     age = staff[1]
#     salary = staff[2]
#     print(f"我叫{name}，今年{age}岁，每月税后薪资{salary}元。")


# def staff_info(name, age, salary):
#     msg = f"我叫{name}，今年{age}岁，每月税后薪资{salary}元。"
#     if salary>=10000:
#         print(msg+"薪资等级：高")
#     elif salary<10000 and salary>=5000:
#         print(msg+"输出薪资等级：中")
#     elif salary<5000 and salary>0:
#         print(msg+"薪资等级：低")
#     else:
#         print("输入有误")
#     return msg
# # staff_info("小周",25,9500)
# # staff_info("小吴",20,4200)
# staff_list = [
#     ["小张",24,4800.0],
#     ["阿美",26,11000.0],
#     ["阿强",21,3500.0]
# ]
# for staff in  staff_list:
#     name = staff[0]
#     age = staff[1]
#     salary = staff[2]
#     staff_info(name, age, salary)
"""
自定义迭代器类型
"""
# class Reverse:
#     """对一个序列执行反向循环的迭代器"""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
# # 创建迭代器对象
# rev = Reverse([2, 3, 5, 7, 11, 13, 17, 19])
# for char in rev:
#     print(char)
#
# """
# 回顾生成器 推导式
# """
# from collections.abc import Iterable, Iterator
# list1 = [x for x in range(10)]
# print(list1)
# gen_1 = (x for x in range(10))
# print(gen_1)
# print(isinstance(gen_1, Iterable)) # 生成器属于可迭代对象
# print(isinstance(gen_1, Iterator)) # 生成器也属于迭代器(因为生成器也具备__next__ 以及 __iter__函数)
# for x in gen_1:
#     print(x)
# tup_1 = tuple(x for x in range(10))
# print(tup_1)
# print(isinstance(tup_1, Iterable)) # 元组属于可迭代对象
# print(isinstance(tup_1, Iterator)) # 元组不属于迭代器(因为元组不具备__next__函数)
# for x in tup_1:
#     print(x)
"""
生成器对比普通函数获取多个数据
通过这个案例再次感受生成器按需取用的特点
需求：获取 100万个整数 保存到一个list列表中
# """
# def get_list():
#     list1 = []
#     for i in range(1000000):
#         list1.append(i)
#     return list1
#
# def create_list():
#     for i in range(1000000):
#         yield i
# list1 = get_list() # 一次性获取100万个数据
# print(list1)
# gen_1 = create_list() # 这里只是得到了生成器
# print(gen_1)
# print(next(gen_1)) # 每next一次 得到一次数据
# print(next(gen_1)) # 每next一次 得到一次数据
# print(next(gen_1)) # 每next一次 得到一次数据
# print(next(gen_1)) # 每next一次 得到一次数据
# """
# 使用生成器斐波那契数列
# """
# def fibo(): # 这里指定形参
#     a , b = 0 , 1
#     while True: # 这里书写为有固定次数的循环
#         yield a
#         a , b = b , a + b
# gen_1 = fibo()
# print(next(gen_1))
# print(next(gen_1))
# print(next(gen_1))
# print(next(gen_1))
# print(next(gen_1))
# print(next(gen_1))
# print(next(gen_1))

import re

class Customer:
    """客户类"""

    def __init__(self, id, name, age, phone, email):
        """
        初始化客户信息
        :param id: 客户编号
        :param name: 客户姓名
        :param age: 客户年龄
        :param phone: 客户手机号
        :param email: 客户邮箱
        """
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    @staticmethod
    def check_c_id(c_id):
        """
        检查客户id是否为正整数字
        :param c_id: 客户id
        :return: True/False
        """
        return c_id.isdigit() and int(c_id) > 0
    @staticmethod
    def check_name(c_name):
        """
        检查客户姓名是否为字符串
        :param name: 客户姓名
        :return: True/False
        """
        return isinstance(c_name, str)
    @staticmethod
    def check_age(c_age):
        """
        检查客户年龄是否合法
        :param c_age:
        :return:
        """
        return c_age.isdigit() and 145>int(c_age) > 0

    @staticmethod
    def check_phone(c_phone):
        """
        利用正则表达中国大陆常见手机号格式检查客户手机号是否合法
        :param c_phone:
        :return:
        """

        pattern = r'^1[3-9]\d{9}$'
        return re.match(pattern, c_phone) is not None
    @staticmethod
    def check_email(c_email):
        """
        利用正则表达式检查客户邮箱是否合法
        :param c_email:
        :return:
        """
        pattern = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, c_email) is not None
    def __str__(self):
        return f"客户编号：{self.id<6}，客户姓名：{self.name<10}，客户年龄：{self.age<6}，客户手机号：{self.phone<15}，客户邮箱：{self.email<25}"


"客户管理类"

class CustomerManager:
    """客户管理类"""
    def __init__(self):
        self.customer_name_dict = {}
        self.customer_id_dict = {}
    "6个功能菜单"
    def start(self):
        """启动系统"""
        try:
            while True:
                self.menu()
                choice = input("请输入您的选择：")
                if choice == "1":
                    self.add_customer()
                elif choice == "2":
                    self.show_all_customer()
                elif choice == "3":
                    self.query_customer()
                elif choice == "4":
                    self.delete_customer()
                elif choice == "5":
                    self.update_customer()
                elif choice == "6":
                    print("谢谢使用，再见！")
                    break
                else:
                    print("您输入的选择有误，请重新输入！")
                    continue
        except (EOFError, KeyboardInterrupt, ValueError):
            print("输入的不是数字，请重新输入！")
    def input_customer_info(self):
        for i in range(3):
            c_id = input("请输入客户编号：")
            if  Customer.check_c_id(c_id):
                if c_id in self.customer_id_dict:
                    print(f"客户编号已存在，请重新输入！,你还有{2-i}次机会")
                    return c_id
            else :
                print(f"客户编号不合法，请重新输入！,你还有{2-i}次机会")
            raise ValueError("客户编号输入次数已达上限")



    def input_customer_name(self):
        for i in range(3):
            c_name = input("请输入客户姓名：")
            if Customer.check_name(c_name):
                if c_name in self.customer_name_dict:
                    print(f"客户姓名已存在，请重新输入！,你还有{2-i}次机会")
                    return c_name
            else:
                print(f"客户姓名不合法，请重新输入！,你还有{2-i}次机会")
        raise ValueError("客户姓名输入次数已达上限")

    def input_customer_age(self):
        for i in range(3):
            c_age = input("请输入客户年龄：")
            if Customer.check_age(c_age):
                return c_age
            else:
                print(f"客户年龄不合法，请重新输入！,你还有{2-i}次机会")
        raise ValueError("客户年龄输入次数已达上限")
    def input_customer_phone(self):
        for i in range(3):
            c_phone = input("请输入客户手机号：")
            if Customer.check_phone(c_phone):
                return c_phone
            else:
                print(f"客户手机号不合法，请重新输入！,你还有{2-i}次机会")
        raise ValueError("客户手机号输入次数已达上限")
    def input_customer_email(self):
        for i in range(3):
            c_email = input("请输入客户邮箱：")
            if Customer.check_email(c_email):
                return c_email
            else:
                print(f"客户邮箱不合法，请重新输入！,你还有{2-i}次机会")
        raise ValueError("客户邮箱输入次数已达上限")


    def add_customer(self):
        """添加客户"""
        try:
            c_id = self.input_customer_info()
            c_name = self.input_customer_name()
            c_age = self.input_customer_age()
            c_phone = self.input_customer_phone()
            c_email = self.input_customer_email()

            customer = Customer(c_id, c_name, c_age, c_phone, c_email)
            self.customer_id_dict[c_id] = customer
            self.customer_name_dict[c_name] = customer
            print("客户添加成功！")
        except ValueError as e:
            print(e)
            return None

    def show_all_customer(self):
        """显示所有客户"""
        if not self.customer_id_dict:
            print("没有客户信息！")
            return
        print("客户信息如下：")
        for customer in self.customer_id_dict.values():
            print(customer)

    def query_customer(self):
        """查询客户"""
        c_id = input("请输入要查询的客户编号：")
        if c_id in self.customer_id_dict:
            print(self.customer_id_dict[c_id])
        else:
            print("没有找到该客户信息！")
    def delete_customer(self):
        """删除客户"""
        c_id = input("请输入要删除的客户编号：")
        if c_id in self.customer_id_dict:
            customer = self.customer_id_dict[c_id]
            del self.customer_id_dict[c_id]
            del self.customer_name_dict[customer.name]
            print("客户删除成功！")
        else:
            print("没有找到该客户信息！")


    def update_customer_id(self,c_id):
        for i in range(3):
            new_c_id = input(f"请输入客户的新编号({c_id})：")
            if new_c_id == "":
                return c_id
            if Customer.check_c_id(new_c_id):
                if new_c_id in self.customer_id_dict and new_c_id != c_id:
                    print(f"编号已存在，请重新输入，你还有{2-i}次机会")
                else:
                    return new_c_id
            else:
                print(f"编号格式错误，请重新输入，你还有{2-i}次机会")
        raise ValueError("输入错误次数过多")
    def update_customer_name(self,c_name):
        for i in range(3):
            new_c_name = input(f"请输入客户的新姓名({c_name})：")
            if new_c_name == "":
                return c_name
            if Customer.check_name(new_c_name):
                if new_c_name in self.customer_name_dict and new_c_name != c_name:
                    print(f"姓名已存在，请重新输入，你还有{2-i}次机会")
                else:
                    return new_c_name
            else:
                print(f"姓名格式错误，请重新输入，你还有{2-i}次机会")
        raise ValueError("输入错误次数过多")
    def update_customer_age(self,c_age):
        for i in range(3):
            new_c_age = input(f"请输入客户的新年龄({c_age})：")
            if new_c_age == "":
                return c_age
            if Customer.check_age(new_c_age):
                return new_c_age
            else:
                print(f"年龄格式错误，请重新输入，你还有{2-i}次机会")
        raise ValueError("输入错误次数过多")
    def update_customer_phone(self,c_phone):
        for i in range(3):
            new_c_phone = input(f"请输入客户的新手机号({c_phone})：")
            if new_c_phone == "":
                return c_phone
            if Customer.check_phone(new_c_phone):
                return new_c_phone
            else:
                print(f"手机号格式错误，请重新输入，你还有{2-i}次机会")
        raise ValueError("输入错误次数过多")
    def update_customer_email(self,c_email):
        for i in range(3):
            new_c_email = input(f"请输入客户的新邮箱({c_email})：")
            if new_c_email == "":
                return c_email
            if Customer.check_email(new_c_email):
                return new_c_email
            else:
                print(f"邮箱格式错误，请重新输入，你还有{2-i}次机会")
        raise ValueError("输入错误次数过多")
    def update_customer(self):
        """根据id和name修改客户信息"""
        for i in range(3):
            c_id_name = input("请输入要修改的客户编号或姓名：")
            cus=self.customer_id_dict.get(c_id_name) 
            if cus is None:
                cus=self.customer_name_dict.get(c_id_name)               
            print(cus)
            if cus is not None:
                c_id=cus.id
                c_name=cus.name
                print(f"客户信息如下：\n{cus}")
                try:
                    c_id = self.update_customer_id(c_id)
                    c_name = self.update_customer_name(c_name)
                    c_age = self.update_customer_age(cus.age)
                    c_phone = self.update_customer_phone(cus.phone)
                    c_email = self.update_customer_email(cus.email)
                    cus = Customer(c_id, c_name, c_age, c_phone, c_email)
                    self.customer_id_dict[c_id] = cus
                    self.customer_name_dict[c_name] = cus
                    print("客户信息修改成功！")
                    return None
                except ValueError as e:
                        print(e)
                        return None
            else:
                print(f"没有找到该客户信息，请重新输入，你还有{2-i}次机会") 
    def menu(self):
        """显示菜单"""
        print("-" * 50)
        print("欢迎使用客户管理系统")
        print("1. 添加客户")
        print("2. 显示所有客户")
        print("3. 查询客户")
        print("4. 删除客户")
        print("5. 修改客户")
        print("6. 退出系统")
        print("-" * 50)
if __name__ == "__main__":
    manager = CustomerManager()
    manager.start()















































