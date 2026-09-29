# class Person:
#     """演示常见特殊方法的类"""
    
#     # (1) __new__(): 创建实例对象时第一个调用的方法
#     def __new__(cls, *args, **kwargs):
#         print(f"1. 调用 __new__ 方法，创建 {cls.__name__} 的实例")
#         instance = super().__new__(cls)
#         return instance
    
#     # (2) __init__(): 对象属性的初始化方法，创建对象时自动调用
#     def __init__(self, name, age):
#         print("2. 调用 __init__ 方法，初始化对象")
#         self.name = name
#         self.age = age
    
#     # (3) __del__(): 对象销毁时调用的方法
#     def __del__(self):
#         print(f"7. 调用 __del__ 方法，销毁对象: {self.name}")
    
#     # (4) __str__(): str(对象)、print(对象)、format(对象)自动调用
#     def __str__(self):
#         print("5. 调用 __str__ 方法")
#         return f"姓名：{self.name}, 年龄：{self.age}"
    
#     # (5) __repr__(): repr(对象)、交互式解释器直接输入对象、调试工具自动调用
#     def __repr__(self):
#         print("6. 调用 __repr__ 方法")
#         return f"Person(name='{self.name}', age={self.age})"
    
#     # (6) __getattribute__(): 属性访问拦截器，获取对象属性值时自动调用
#     def __getattribute__(self, field_name):
#         print(f"4. 访问属性 '{field_name}' (通过 __getattribute__ 拦截)")
#         # 必须使用 super() 来避免无限递归
#         return super().__getattribute__(field_name)
    
#     # (7) __setattr__(): 属性赋值拦截器，修改属性值的时候会自动调用
#     def __setattr__(self, field_name, field_value):
#         print(f"3. 赋值属性 '{field_name}' = {field_value} (通过 __setattr__ 拦截)")
#         if field_name == "age" and field_value <= 0:
#             super().__setattr__(field_name, 0)
#         else:
#             super().__setattr__(field_name, field_value)


# # ========== 演示过程 ==========
# print("=== 创建对象 ===")
# obj = Person("张三", -18)

# print("\n=== 获取属性值 ===")
# name_value = obj.name
# print("name_value:", name_value)
# age_value = obj.age
# print("age_value:", age_value)

# print("\n=== 使用 str() 和 repr() ===")
# print(obj)                    # 自动调用 __str__()
# print("repr(obj):", repr(obj)) # 自动调用 __repr__()

# print("\n=== 删除对象引用 ===")
# del obj

# print("\n=== 程序结束 ===")


# class student:
#     school_name="第一中学"
#     student_count=0

#     def__init__(self,name,age,class_name):
#     self.name=name
#     self.age=age
#     self.class_name=class_name
#     student_count +=1
#     def introduce(self):
#         print(f"姓名: {self.name}, 年龄: {self.age}, 班级: {self.class_name}, 学校: {student.school_name}")
#     def have_birthday(self):
#         self.age += 1
#         print(f"祝{self.name}生日快乐！现在年龄是{self.age}岁。") # type: ignore
#     @classmethod
#     def change_school(cls, new_name):
#         cls.school_name =new_name
#         print(f"学校名称已修改为: {cls.school_name}")
#     def get_student_count(cls):
#         return print(f"学生总数为{cls.student_count}")
#     def is_valid_age(age):
#         return 6<=age<-18 # pyright: ignore[reportOperatorIssue]

# class ShoppingCart:
#     store_name="默认商店"
#     total_carts=0
#     def __inif__(self，)
        

# num = 1 # 定义一个循环变量
# count = 0  # 计数器变量
# while num <= 100 :
#  # 判断当前编译出来的数是否能被3整除
#     if num % 3 == 0 :
#  # 如果能被3整除,将这个数打印出来
#         print(num,end ="\t")
#         count += 1
#         if count % 5 == 0 :
#         print()
# num += 1 # 改变循环变量

# def multiply_list(numbers):
#     result = 1
#     for num in numbers:
#         result *= num
#     return result

# # 调用函数
# print(multiply_list([2, 3, 4]))


"""
客户模块 客户类
属性：编号 名字 年龄 电话 邮箱
"""
import re


class Customer:
    def __init__(self, c_id, name="None", age="None", phone="None", email="None"):
        self.c_id = c_id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    @staticmethod
    def check_c_id(c_id):
        """校验id是否为纯数字格式"""
        return c_id.isdigit()

    @staticmethod
    def check_name(name):
        """校验名字：允许中文、英文、空格"""
        return bool(re.match(r"^[\u4e00-\u9fa5a-zA-Z\s]+$", name))

    @staticmethod
    def check_age(age):
        """校验年龄：纯数字，且0-150之间"""
        return age.isdigit() and 0 <= int(age) <= 150

    @staticmethod
    def check_phone(phone):
        """校验手机号：1开头，第二位3-9，共11位"""
        return bool(re.match(r"^1[3-9]\d{9}$", phone))

    @staticmethod
    def check_email(email):
        """校验邮箱格式"""
        pattern = r"^[\w!#$%&'*+/=?^`{|}~.-]+@[\w!#$%&'*+/=?^`{|}~.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    def __str__(self):
        return (f"cid:{self.c_id:<10},name:{self.name:<10},"
                f"age:{self.age:<10},phone:{self.phone:<10},email:{self.email:<10}")


"""
客户管理系统模块
此模块将实现所有的CRUD操作
"""
class CMS:
    def __init__(self):
        # 用户信息字典 k：id  v：客户对象 Customer
        self.customer_dict = {}

    def _input_with_retry(self, prompt, check_func, error_msg):
        """通用输入重试逻辑（3次机会），减少重复代码"""
        for i in range(3):
            if i == 2:
                user_input = input(f"最后一次机会，{prompt}")
            else:
                user_input = input(prompt)
            
            if check_func(user_input):
                return user_input
            else:
                print(error_msg)
        
        print("输入错误次数过多，终止操作")
        return False

    def add_customer_id(self):
        customer_id = self._input_with_retry(
            "请输入客户id\n",
            Customer.check_c_id,
            "id必须为纯数字"
        )
        if customer_id is False:
            return False
        
        if customer_id in self.customer_dict:
            print("客户id已存在，不能重复添加")
            return False
        
        return customer_id

    def add_customer_name(self):
        return self._input_with_retry(
            "请输入客户姓名\n",
            Customer.check_name,
            "名字格式不正确"
        )

    def set_customer_age(self):
        customer_age = input("请输入年龄\n")
        if Customer.check_age(customer_age):
            return customer_age
        else:
            print("年龄格式不正确，暂时不添加年龄")
            return "None"

    def set_customer_phone(self):
        customer_phone = input("请输入客户电话\n")
        if Customer.check_phone(customer_phone):
            return customer_phone
        else:
            print("电话格式不正确，暂时不添加电话")
            return "None"

    def set_customer_email(self):
        customer_email = input("请输入邮箱\n")
        if Customer.check_email(customer_email):
            return customer_email
        else:
            print("邮箱格式不正确，暂时不添加邮箱")
            return "None"

    def add_customer(self):
        # ID 和 姓名 是必填项
        if not (customer_id := self.add_customer_id()):
            return
        if not (customer_name := self.add_customer_name()):
            return
        
        # 其余是选填项
        customer_age = self.set_customer_age()
        customer_phone = self.set_customer_phone()
        customer_email = self.set_customer_email()
        
        customer = Customer(customer_id, customer_name, customer_age, customer_phone, customer_email)
        self.customer_dict[customer_id] = customer
        print(f"添加客户 {customer_name} 成功！")

    def delete_customer(self):
        c_id = input("请输入要删除的客户id\n")
        if c_id in self.customer_dict:
            name = self.customer_dict[c_id].name
            del self.customer_dict[c_id]
            print(f"客户 {name} 删除成功")
        else:
            print("客户id不存在")

    def update_customer(self):
        c_id = input("请输入要修改的客户id\n")
        if c_id not in self.customer_dict:
            print("客户id不存在")
            return
        
        customer = self.customer_dict[c_id]
        print(f"当前信息：{customer}")
        print("请输入新信息（直接回车表示不修改）：")
        
        new_name = input("姓名：")
        if new_name and Customer.check_name(new_name):
            customer.name = new_name
        
        new_age = input("年龄：")
        if new_age and Customer.check_age(new_age):
            customer.age = new_age
        
        new_phone = input("电话：")
        if new_phone and Customer.check_phone(new_phone):
            customer.phone = new_phone
        
        new_email = input("邮箱：")
        if new_email and Customer.check_email(new_email):
            customer.email = new_email
        
        print("修改成功")

    def query_customer(self):
        c_id = input("请输入要查询的客户id\n")
        if c_id in self.customer_dict:
            print(self.customer_dict[c_id])
        else:
            print("客户id不存在")

    def show_all_customer(self):
        if len(self.customer_dict) == 0:
            print("暂无客户信息")
        else:
            for customer in self.customer_dict.values():
                print(customer)

    def display_menu(self):
        print("""
    `********************客户管理系统*********************
    1.添加客户
    2.删除客户
    3.修改客户
    4.查询客户
    5.显示所有客户
    6.退出
    """)`

    def start(self):
        try:
            while True:
                self.display_menu()
                choice = input("请输入选项\n")
                match choice:
                    case "1":
                        self.add_customer()
                    case "2":
                        self.delete_customer()
                    case "3":
                        self.update_customer()
                    case "4":
                        self.query_customer()
                    case "5":
                        self.show_all_customer()
                    case "6":
                        print("退出系统")
                        break
                    case _:
                        print("输入错误，请重新输入")
        except (EOFError, KeyboardInterrupt):
            print("\n退出系统")


if __name__ == '__main__':
    cms = CMS()
    cms.start()