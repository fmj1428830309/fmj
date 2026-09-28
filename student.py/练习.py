## 练习1：学生信息管理系统
'''
**题目要求：**

1. 创建一个Student类，包含以下内容：
   - 类属性：`school_name`（学校名称，初始值为"第一中学"）、`student_count`（学生总数，初始值为0）
   - 实例属性：`name`（姓名）、`age`（年龄）、`class_name`（班级）
2. 在`__init__`方法中：
   - 初始化实例属性
   - 每次创建学生对象时，让`student_count`自动增加1
3. 定义实例方法：
   - `introduce(self)`：打印学生的所有个人信息
   - `have_birthday(self)`：让学生年龄增加1岁，并打印生日祝福
4. 定义类方法：
   - `change_school(cls, new_name)`：修改学校名称
   - `get_student_count(cls)`：返回当前学生总数
5. 定义静态方法：
   - `is_valid_age(age)`：判断年龄是否在6-18岁之间（包含边界）
6. 创建至少3个学生对象，并依次：
   - 调用`introduce()`方法
   - 为其中一个学生调用`have_birthday()`方法
   - 使用类方法修改学校名称
   - 使用类方法查看学生总数
   - 使用静态方法验证几个不同年龄'''
class student:
    school_name = "第一中学"
    student_count = 0

    def __init__(self, name, age, class_name):
        self.name = name
        self.age = age
        self.class_name = class_name
        student.student_count += 1

    def introduce(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 班级: {self.class_name}, 学校: {student.school_name}")

    def have_birthday(self):
        self.age += 1
        print(f"祝{self.name}生日快乐！现在年龄是{self.age}岁。")

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
        print(f"学校名称已修改为: {cls.school_name}")

    @classmethod
    def get_student_count(cls):
        return cls.student_count

    @staticmethod
    def is_valid_age(age):
        return 6 <= age <= 18
student1 = student("张三", 15, "高一(1)班")
student2 = student("李四", 17, "高二(2)班")
student3 = student("王五", 14, "高一(3)班")
student1.introduce()
student2.introduce()
student3.introduce()
student1.have_birthday()
student.change_school("第二中学")
print(f"学生总数: {student.get_student_count()}")
print(f"年龄是否有效: {student.is_valid_age(student1.age)}")
print(f"年龄是否有效: {student.is_valid_age(student2.age)}")
print(f"年龄是否有效: {student.is_valid_age(student3.age)}")
## 练习2：简单的购物车系统
'''
**题目要求：**

1. 创建一个`ShoppingCart`类，包含以下内容：
   - 类属性：`store_name`（商店名称）、`total_carts`（创建的购物车总数）
   - 实例属性：`owner`（拥有者）、`items`（物品列表，初始为空）、`total_price`（总价，初始为0）
2. 定义实例方法：
   - `add_item(self,item_name, price)`：添加物品到购物车（更新items列表和total_price）
   - `remove_item(self,item_name)`：从购物车中移除指定物品
   - `show_cart(self)`：显示购物车中的所有物品和总价
3. 定义类方法：
   - `set_store_name(cls, new_name)`：修改商店名称
   - `show_total_carts(cls)`：显示创建的购物车总数
4. 定义静态方法：
   - `calculate_discount(price, discount_rate)`：计算折扣后的价格
5. 创建2个购物车对象（不同拥有者），并测试：
   - 分别添加3-4件物品
   - 从一个购物车中移除一件物品
   - 显示两个购物车的内容
   - 修改商店名称并验证
   - 使用静态方法计算某个物品的折扣价'''
class ShoppingCart:
    store_name = "默认商店"
    total_carts = 0

    def __init__(self, owner):
        self.owner = owner
        self.items = []
        self.total_price = 0
        ShoppingCart.total_carts += 1

    def add_item(self, item_name, price):
        self.items.append((item_name, price))
        self.total_price += price

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                self.total_price -= item[1]
                break

    def show_cart(self):
        print(f"购物车拥有者: {self.owner}")
        print("物品列表:")
        for item in self.items:
            print(f"  - {item[0]}: ¥{item[1]}")
        print(f"总价: ¥{self.total_price}")

    @classmethod
    def set_store_name(cls, new_name):
        cls.store_name = new_name

    @classmethod
    def show_total_carts(cls):
        print(f"创建的购物车总数: {cls.total_carts}")

    @staticmethod
    def calculate_discount(price, discount_rate):
        return price * (1 - discount_rate)
shopping_cart1 = ShoppingCart("Alice")
shopping_cart2 = ShoppingCart("Bob")
shopping_cart1.add_item("苹果", 5,)
shopping_cart1.add_item("香蕉", 3,)
shopping_cart1.add_item("橙子", 4,)
shopping_cart2.add_item("牛奶", 10,)
shopping_cart2.add_item("面包", 6,)
shopping_cart2.add_item("鸡蛋", 8,)
shopping_cart1.remove_item("香蕉")
shopping_cart1.show_cart()
shopping_cart2.show_cart()
ShoppingCart.set_store_name("新商店")
print(f"商店名称已修改为: {ShoppingCart.store_name}")
student_discount_price = ShoppingCart.calculate_discount(5, 0.2)
print(f"折扣后的价格: ¥{student_discount_price}")
'''## 练习3：图书管理系统

**题目要求：**

1. 创建一个`Book`类，包含以下内容：
   - 类属性：`library_name`（图书馆名称）、`total_books`（图书总数）
   - 实例属性：`title`（书名）、`author`（作者）、`is_borrowed`（是否借出，默认为False）
2. 定义实例方法：
   - `borrow(self)`：借出图书（如果未被借出则改为借出状态，否则打印提示信息）
   - `return_book(self)`：归还图书（改为未借出状态）
   - `display_info(self)`：显示图书信息
3. 定义类方法：
   - `change_library_name(cls, new_name)`：修改图书馆名称
   - `get_total_books(cls)`：获取图书总数
4. 定义静态方法：
   - `is_valid_book(book_title)`：判断书名是否有效（长度大于0且不为空）
5. 创建3个图书对象，并进行以下操作：
   - 借出其中一本书
   - 尝试借出同一本书（应该提示已被借出）
   - 归还一本书
   - 显示所有图书信息
   - 修改图书馆名称
   - 使用静态方法验证几个书名'''
class Book:
    library_name = "市图书馆"
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        Book.total_books += 1

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"《{self.title}》已被借出。")
        else:
            print(f"《{self.title}》已被借出，无法再次借出。")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"《{self.title}》已归还。")
        else:
            print(f"《{self.title}》未被借出，无需归还。")

    def display_info(self):
        status = "已借出" if self.is_borrowed else "可借"
        print(f"书名: {self.title}, 作者: {self.author}, 状态: {status}")

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name
        print(f"图书馆名称已修改为: {cls.library_name}")

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @staticmethod
    def is_valid_book(book_title):
        return len(book_title.strip()) > 0
book1 = Book("Python编程", "张三")
book2 = Book("数据结构与算法", "李四")
book3 = Book("人工智能导论", "王五")
book1.borrow()
book1.borrow()
book1.return_book()
book1.display_info()
book2.display_info()
book3.display_info()
Book.change_library_name("市中心图书馆")
print(f"图书总数: {Book.get_total_books()}")    
book_titles = ["Python编程", "", "  ", "数据结构与算法"]
for title in book_titles:
    print(f"书名 '{title}' 是否有效: {Book.is_valid_book(title)}")
'''## 练习4：动态修改类和实例

**题目要求：**

1. 创建一个`Car`类，初始包含：
   - 类属性：`wheels`（轮子数量，默认为4）
   - 实例属性：`brand`（品牌）、`color`（颜色）
   - 实例方法：`drive(self)`（打印"汽车正在行驶"）
2. 进行以下动态操作练习：
   - **动态添加实例属性**：
     - 为某个汽车对象添加`engine`属性（发动机型号）
   - **动态修改实例属性**：
     - 修改某个汽车对象的颜色
   - **动态删除实例属性**：
     - 删除某个汽车对象的颜色属性
   - **动态添加类属性**：
     - 为Car类添加`fuel_type`属性（燃料类型）
   - **动态修改类属性**：
     - 修改Car类的`wheels`属性
   - **动态添加方法**：
     - 为Car类动态添加一个类方法`show_info(cls)`
     - 为某个汽车对象动态添加一个实例方法`stop(self)`
   - **动态删除方法**：
     - 删除某个对象的方法或类的某个方法
3. 每一步操作后，验证属性/方法是否存在并展示效果'''
class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print("汽车正在行驶")
car1 = Car("Toyota", "红色")
car2 = Car("Honda", "白色")
# 动态添加实例属性
car1.engine = "V6"
print(f"动态添加实例属性: {car1.engine}")
# 动态修改实例属性
car1.color = "蓝色"
print(f"动态修改实例属性: {car1.color}")
# 动态删除实例属性
#del car1.color
print(f"动态删除实例属性: {hasattr(car1, 'color')}")
# 动态添加类属性
Car.fuel_type = "汽油"
print(f"动态添加类属性: {Car.fuel_type}")
# 动态修改类属性
Car.wheels = 6
print(f"动态修改类属性: {Car.wheels}")
import types

def show_info(cls):
    print(f"品牌: {cls.brand}, 颜色: {cls.color}, 轮子数量: {cls.wheels}, 燃料类型: {cls.fuel_type}")
car1.show_info=types.MethodType(show_info, car1)
car1.show_info()
def stop(self):
    print("汽车已停止")
car1.stop = types.MethodType(stop, car1)
car1.stop()
del car1.stop
print(f"动态删除方法: {hasattr(car1, 'stop')}")
'''## 练习5：综合练习 - 银行账户系统

**题目要求：**

1. 创建一个`BankAccount`类，包含以下内容：
   - 类属性：`bank_name`（银行名称）、`total_accounts`（账户总数）、`interest_rate`（利率，默认为0.03）
   - 实例属性：`account_number`（账号）、`owner`（户主）、`balance`（余额，初始为0）
2. 定义实例方法：
   - `deposit(self,amount)`：存款（增加余额）
   - `withdraw(self,amount)`：取款（检查余额是否足够）
   - `check_balance(self)`：查询余额
   - `apply_interest(self)`：应用利率计算利息并加到余额
3. 定义类方法：
   - `change_interest_rate(cls, new_rate)`：修改利率
   - `get_total_accounts(cls)`：获取总账户数
   - `create_account(cls, owner)`：创建账户并自动生成账号（账号规则：BANK + 10001 + 序号）
4. 定义静态方法：
   - `validate_amount(amount)`：验证金额是否为正数
   - `format_currency(amount)`：将金额格式化为货币格式（如：¥1,234.56）
5. 创建3个账户并进行以下操作：
   - 存款操作
   - 取款操作
   - 查询余额
   - 应用利息
   - 修改利率后再次应用利息
   - 使用静态方法验证金额和格式化金额'''
class BankAccount:
    bank_name = "中国银行"
    total_accounts = 0
    interest_rate = 0.03

    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self.balance = 0
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.balance += amount
            print(f"{self.owner}存入: {self.format_currency(amount)}，当前余额: {self.format_currency(self.balance)}")
        else:
            print("存款金额必须为正数。")

    def withdraw(self, amount):
        if self.validate_amount(amount):
            if amount <= self.balance:
                self.balance -= amount
                print(f"{self.owner}取出: {self.format_currency(amount)}，当前余额: {self.format_currency(self.balance)}")
            else:
                print("余额不足，无法取款。")
        else:
            print("取款金额必须为正数。")

    def check_balance(self):
        print(f"{self.owner}的当前余额: {self.format_currency(self.balance)}")

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"{self.owner}应用利息: {self.format_currency(interest)}，当前余额: {self.format_currency(self.balance)}")

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"利率已修改为: {cls.interest_rate * 100}%")

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @classmethod
    def create_account(cls, owner):
        account_number = f"BANK{10001 + cls.total_accounts}"
        return cls(account_number, owner)

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    @staticmethod
    def format_currency(amount):
        return f"¥{amount:,.2f}"
transaction1 = BankAccount.create_account("张三")
transaction2 = BankAccount.create_account("李四")
transaction3 = BankAccount.create_account("王五")
transaction1.deposit(1000)
transaction1.withdraw(200)
transaction2.deposit(1500)
transaction2.withdraw(500)
transaction3.deposit(2000)
transaction3.withdraw(1000) 
transaction1.check_balance()
transaction2.check_balance()
transaction3.check_balance()
transaction1.apply_interest()
BankAccount.change_interest_rate(0.05)
transaction1.apply_interest()
valid_amounts = [100, -50, 0, 200]
for amount in valid_amounts:
    print(f"金额 {amount} 是否有效: {BankAccount.validate_amount(amount)}")
formatted_amount = BankAccount.format_currency(1234567.89)
print(f"格式化金额: {formatted_amount}")
'''## 练习题1：银行账户系统（封装）

创建一个银行账户类 `BankAccount`，实现基本的封装特性：

**要求：**

- 私有属性：`__account_number`（账号）、`__balance`（余额）、`__password`（密码）
- 提供公开方法：
  - `deposit(amount, password)`：存款（需要验证密码）
  - `withdraw(amount, password)`：取款（需要验证密码）
  - `check_balance(password)`：查询余额（需要验证密码）
  - `set_password(old_password, new_password)`：修改密码，修改密码时，还得输入旧密码用于验证
- 设置合理的属性访问控制，不允许直接访问和修改私有属性

**提示：** 使用双下划线前缀实现私有属性'''
class BankAccount:
    def __init__(self, account_number, password):
        self.__account_number = account_number
        self.__balance = 0
        self.__password = password
    def deposit(self, amount, password):
        if password==self.__password:
            if amount>0:
                self.__balance+=amount
                print(f"存款成功，当前余额为：{self.__balance}")
            else:
                print("存款金额必须为正数")
    def withdraw(self, amount, password):
        if password==self.__password:
            if amount>0:
                if amount<=self.__balance:
                    self.__balance-=amount
                    print(f"取款成功，当前余额为：{self.__balance}")
                else:
                    print("余额不足")
            else:
                print("取款金额必须为正数")
    def check_balance(self, password):
        if password==self.__password:
            print(f"当前余额为：{self.__balance}")
    def set_password(self, old_password, new_password):
        if old_password==self.__password:
            self.__password=new_password
            print("密码修改成功")
'''## 练习题2：动物继承体系（继承）

创建一个动物继承体系，展示基本的继承特性：

**要求：**

- 基类 `Animal`：
  - 属性：`name`、`age`
  - 方法：`eat()`、`sleep()`（打印通用信息）
- 派生类：
  - `Dog`：添加方法 `bark()`
  - `Cat`：添加方法 `meow()`
  - `Bird`：添加方法 `fly()`，并重写 `eat()` 方法（鸟类吃虫子的特殊行为）
- 每个派生类都应调用父类的初始化方法'''
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name}正在吃东西")
    def sleep(self):
        print(f"{self.name}正在睡觉")
class Dog(Animal):
    def bark(self):
        print(f"{self.name}正在叫：汪汪汪")
class Cat(Animal):
    def meow(self):
        print(f"{self.name}正在叫：喵喵喵")
class Bird(Animal):
    def fly(self):
        print(f"{self.name}正在飞翔")
    def eat(self):
        print(f"{self.name}正在吃虫子")
dog = Dog("小黑", 3)
cat = Cat("小白", 2)
bird = Bird("小黄", 1)
dog.eat()
dog.sleep()
dog.bark()
cat.eat()
cat.sleep()
cat.meow()
bird.eat()
bird.sleep()
bird.fly()
'''## 练习题3：图形面积计算（多态）

创建一个图形类体系，展示多态特性：

**要求：**

- 基类 `Shape`：
  - 定义方法 `area()` 和 `perimeter()`，方法体用pass表示
- 派生类：
  - `Rectangle`（矩形）：属性 `width`、`height`
  - `Circle`（圆形）：属性 `radius`
  - `Triangle`（三角形）：属性 `a`、`b`、`c`（三边长）
- 创建函数 `print_shape_info(shape)`，接收任何形状对象并打印其面积和周长
- 演示多态：用不同形状对象调用同一函数'''
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * self.radius ** 2
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        import math
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c

def print_shape_info(shape):
    print(f"面积：{shape.area()}")
    print(f"周长：{shape.perimeter()}")

# 演示多态
rectangle = Rectangle(5, 3)
circle = Circle(2)
triangle = Triangle(3, 4, 5)

print("矩形信息：")
print_shape_info(rectangle)

print("圆形信息：")
print_shape_info(circle)

print("三角形信息：")
print_shape_info(triangle)
'''## 练习题4：员工管理系统（组合封装与继承）

设计一个员工管理系统，综合运用封装和继承：

**要求：**

- 基类 `Employee`（封装）：
  - 私有属性：`__name`、`__id`、`__base_salary`
  - 公开方法：`get_details()`、`calculate_salary()`（基本工资）
- 派生类：
  - `Manager`：额外属性 `bonus`（奖金），重写 `calculate_salary()`
  - `Developer`：额外属性 `project_count`，重写 `calculate_salary()`（按项目数量计算）
  - `Intern`：额外属性 `mentor`（指导人），重写 `calculate_salary()`（固定津贴）
- 公司类 `Company`（组合）：
  - 属性：员工列表
  - 方法：`add_employee()`、`remove_employee()`、`get_total_salary()`、`list_all_employees()`
  '''
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.__name = name
        self.__id = emp_id
        self.__base_salary = base_salary

    def get_details(self):
        return f"姓名: {self.__name}, 工号: {self.__id}, 基本工资: {self.__base_salary}"

    def calculate_salary(self):
        return self.__base_salary
class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, bonus):
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus
class Developer(Employee):
    def __init__(self, name, emp_id, base_salary, project_count):
        super().__init__(name, emp_id, base_salary)
        self.project_count = project_count

    def calculate_salary(self):
        return super().calculate_salary() + (self.project_count * 500)  # 每个项目额外500元
class Intern(Employee):
    def __init__(self, name, emp_id, base_salary, mentor):
        super().__init__(name, emp_id, base_salary)
        self.mentor = mentor

    def calculate_salary(self):
        return super().calculate_salary() + 1000  # 固定津贴1000元  
class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.get_details().split(", ")[1].split(": ")[1] != emp_id]

    def get_total_salary(self):
        return sum(emp.calculate_salary() for emp in self.employees)

    def list_all_employees(self):
        for emp in self.employees:
            print(emp.get_details())
company = Company()
manager = Manager("张经理", "M001", 8000, 2000)
developer = Developer("李开发", "D001", 6000, 3)
intern = Intern("王实习", "I001", 3000, "张经理")
company.add_employee(manager)
company.add_employee(developer)
company.add_employee(intern)
company.list_all_employees()
print(f"公司总工资支出: {company.get_total_salary()}")
company.remove_employee("D001")
company.list_all_employees()
'''## 练习题5：图书馆借阅系统（综合练习）

设计一个图书馆借阅系统，综合运用三大特性：

**要求：**

- 基类 `LibraryItem`（封装）：
  - 私有属性：`__item_id`、`__title`、`__is_borrowed`
  - 方法：
    - `borrow()`：修改`__is_borrowed`为True
    - `return_item()`：修改`__is_borrowed`为False
    - ``get_info()`：编号：xx，名称：xx，是否可借阅：是/否
- 派生类（继承与多态）：
  - `Book`：额外属性 `author`、`pages`，重写 `get_info()`
  - `DVD`：额外属性 `director`、`duration`，重写 `get_info()`
  - `Magazine`：额外属性 `issue_number`，重写 `get_info()`
- 类 `Library`（组合）：
  - 属性：物品列表
  - 方法：`add_item()`、`remove_item()`、`search_by_title()`、`display_available_items()`
- 实现多态：`display_item_info(item)` 函数能正确显示任何类型物品的信息'''
class LibraryItem:
    def __init__(self, item_id, title):
        self.__item_id = item_id
        self.__title = title
        self.__is_borrowed = False
    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            print(f"{self.__title} 已被借出。")
        else:
            print(f"{self.__title} 已被借出，无法再次借出。")
    def return_item(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            print(f"{self.__title} 已归还。")
        else:
            print(f"{self.__title} 未被借出，无需归还。")
    def get_info(self):
        #获取物品信息
        status = "否" if self.__is_borrowed else "是"
        return f"编号: {self.__item_id}, 名称: {self.__title}, 是否可借阅: {status}"
class Book(LibraryItem):
    def __init__(self, item_id, title, author, pages):
        #初始化图书
        super().__init__(item_id, title)
        self.author = author
        self.pages = pages
    def get_info(self):
        #获取图书信息
        base_info = super().get_info()
        return f"{base_info}, 作者: {self.author}, 页数: {self.pages}"
class DVD(LibraryItem):
    def __init__(self, item_id, title, director, duration):
        #初始化DVD
        super().__init__(item_id, title)
        self.director = director
        self.duration = duration
    def get_info(self):
        #获取DVD信息
        base_info = super().get_info()
        return f"{base_info}, 导演: {self.director}, 时长: {self.duration}分钟"
class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number):
        #初始化杂志
        super().__init__(item_id, title)
        self.issue_number = issue_number
    def get_info(self):
        #获取杂志信息
        base_info = super().get_info()
        return f"{base_info}, 期号: {self.issue_number}"
class Library:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        #添加物品到图书馆
        self.items.append(item)
    def remove_item(self, item_id):
        #移除指定编号的物品
        self.items = [item for item in self.items if item.get_info().split(", ")[0].split(": ")[1] != item_id]
    def search_by_title(self, title):
        #根据标题搜索物品
        return [item for item in self.items if title.lower() in item.get_info().lower()]
    def display_available_items(self):
        #显示所有可借阅的物品
        for item in self.items:
            if "是" in item.get_info():
                print(item.get_info())
library = Library()
book1 = Book("B001", "Python编程", "张三", 300)
dvd1 = DVD("D001", "电影之旅", "李四", 120)
magazine1 = Magazine("M001", "科技杂志", "2024年6月")
library.add_item(book1)
library.add_item(dvd1)
library.add_item(magazine1)
library.display_available_items()
book1.borrow()
library.display_available_items()


'''1. 编写一段 Python 代码，尝试将字符串 "123abc" 转换为整数，如果转换失败，捕获 ValueError 异常，将异常信息记录到一个文本文件 error.log 中。'''
'''try:
    num = int("123abc")
    print(num)
except ValueError as e:
    with open("error.log", "a", encoding="utf-8") as f:
    
        f.write(f"转换错误: str(e)\n")
    print(f"转换错误: {e}")'''


'''2. 定义一个函数check_age，该函数接受一个年龄参数。如果年龄小于 0，抛出一个自定义异常InvalidAgeError；如果年龄大于 120，抛出UnrealisticAgeError。这两个自定义异常类都继承自Exception类。调用该函数并传入一个不合法的年龄值，捕获并处理异常。'''
class InvalidAgeError(Exception):
    pass

class UnrealisticAgeError(Exception):
    pass

def check_age(age):
    try:
        if not (0 <= age <= 120):
            raise InvalidAgeError("年龄必须在0到120之间")
        print(f"年龄 {age} 是有效的。")
        if age>120:
            raise UnrealisticAgeError("年龄不能大于120")
    except InvalidAgeError as e:
        print(f"年龄错误: {e}")
    except UnrealisticAgeError as e:
        print(f"年龄错误: {e}")
check_age(25)  # 有效年龄
check_age(-5)  # 无效年龄
check_age(130)  # 不现实的年龄
'''### 练习题 1：datetime 库 - 日期计算器

题目要求：编写一个程序，实现以下功能：

1. 接收用户输入的一个起始日期（格式：YYYY-MM-DD）和一个天数 n；
2. 计算并输出起始日期加上 n 天后的日期；
3. 计算并输出起始日期是星期几（中文显示：星期一 / 星期二...）；
4. 计算并输出起始日期所在月份的总天数。'''
date=input("请输入日期（格式：YYYY-MM-DD）：")
day=int(input("请输入天数："))
try:
    from datetime import datetime, timedelta
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    new_date = date_obj + timedelta(days=day)
    print(f"{day}天后的日期是: {new_date.strftime('%Y-%m-%d')}")
except ValueError as e:
    print(f"日期格式错误: {e}")
'''### 练习题 2：string 库 - 随机验证码生成器

题目要求：编写一个函数，生成指定长度的随机验证码，要求：

1. 验证码包含大写字母、小写字母和数字；
2. 长度由用户输入指定（范围：4-8 位）；
3. 确保每个验证码中至少包含 1 个大写字母、1 个小写字母和 1 个数字；
4. 输出生成的验证码。'''
import string
import random

def generate_code(length):
    if not (4 <= length <= 8):
        return None
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    all_chars = upper + lower + digits
    
    code = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits)
    ]
    for _ in range(length - 3):
        code.append(random.choice(all_chars))
    
    random.shuffle(code)
    return ''.join(code)


# ========== 用 try 持续输入，直到合法 ==========
while True:
    try:
        length = int(input("请输入验证码长度（4-8位）："))
        
        if not (4 <= length <= 8):
            print("❌ 长度必须在 4-8 位之间！请重新输入。\n")
            continue
        
        # 合法输入，生成验证码并退出
        code = generate_code(length)
        print(f"✅ 生成的验证码：{code}")
        break
        
    except ValueError:
        print("❌ 请输入有效的整数！请重新输入。\n")
'''### 练习题 3：math 库 - 几何计算工具

题目要求：编写一个程序，实现以下功能：

1. 让用户选择计算类型：圆的面积、球体的体积、直角三角形的斜边长度；

   ```python
   	print("=== 几何计算工具 ===")
       print("1. 计算圆的面积")
       print("2. 计算球体的体积")
       print("3. 计算直角三角形的斜边长度")
   ```

2. 根据选择的类型，接收对应的输入参数（如圆的半径、三角形的两条直角边）；

   例如：选择1.计算圆的面积后，让用户输入圆的半径

3. 使用 math 库的函数完成计算，结果保留 2 位小数；

4. 输出计算结果。
'''
def math(yuan):
    print("=== 几何计算工具 ===")
    print("1. 计算圆的面积")
    print("2. 计算球体的体积")
    print("3. 计算直角三角形的斜边长度")
    math_choice = input("请选择计算类型（1/2/3）：")
    if math_choice == "1":
        radius = float(input("请输入圆的半径："))
        area = math.pi * radius ** 2
        print(f"圆的面积为: {area:.2f}")
    elif math_choice == "2":
        radius = float(input("请输入球体的半径："))
        volume = (4/3) * math.pi * radius ** 3
        print(f"球体的体积为: {volume:.2f}")
    elif math_choice == "3":
        a = float(input("请输入直角三角形的两条直角边长度（用空格分隔）："))
        b = float(input())
        hypotenuse = math.sqrt(a ** 2 + b ** 2)
        print(f"直角三角形的斜边长度为: {hypotenuse:.2f}")

'''

### 练习题 4：综合练习 - 随机抽奖程序

题目要求：编写一个抽奖程序，结合`random`、`datetime`、`string`库，实现：

1. 读取用户输入的抽奖名单（多个名字用逗号分隔）；
2. 生成每个参与者的唯一抽奖码（格式：8 位，前 4 位为随机大写字母，后 4 位为随机数字）；
3. 记录抽奖时间（精确到秒）；
4. 随机抽取 1 名一等奖、2 名二等奖、3 名三等奖；
5. 按格式输出抽奖结果（包含抽奖时间、各奖项获奖者及抽奖码）。'''
def generate_lottery_code():
    upper = string.ascii_uppercase
    digits = string.digits
    code = ''.join(random.choice(upper) for _ in range(4)) + ''.join(random.choice(digits) for _ in range(4))
    return code
def lottery():
    participants_input = input("请输入抽奖名单（用逗号分隔）：")
    participants = [name.strip() for name in participants_input.split(",") if name.strip()]
    
    if len(participants) < 6:
        print("参与者人数不足，至少需要6人。")
        return
    
    lottery_codes = {name: generate_lottery_code() for name in participants}
    draw_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    winners = random.sample(participants, 6)
    first_prize = winners[0]
    second_prizes = winners[1:3]
    third_prizes = winners[3:6]
    
    print(f"\n抽奖时间: {draw_time}")
    print(f"一等奖: {first_prize}，抽奖码: {lottery_codes[first_prize]}")
    print("二等奖:")
    for winner in second_prizes:
        print(f"  - {winner}，抽奖码: {lottery_codes[winner]}")
    print("三等奖:")
    for winner in third_prizes:
        print(f"  - {winner}，抽奖码: {lottery_codes[winner]}")


