# ======================================================================
# Python 面向对象编程 综合练习
# 包含：继承、方法重写、super()、类型注解、异步编程（async/await）
# ======================================================================


# ======================================================================
# 一、继承基础：普通员工 → 实习员工 / 正式员工
# ======================================================================

# 普通员工（父类/基类）
class Staff:
    """
    普通员工类，定义了员工的基本属性和方法。
    后续的「实习员工」和「正式员工」会继承这个类，复用这些代码。
    """

    # __init__ 是构造方法（constructor），创建对象时自动调用
    # self 代表实例本身，必须写在第一个参数位置
    # s_name、s_age、s_salary 是形式参数，s 前缀表示传入的变量
    def __init__(self, s_name, s_age, s_salary):
        self.name = s_name        # 把参数 s_name 的值赋给实例属性 self.name
        self.age = s_age          # 员工年龄
        self.salary = s_salary    # 员工薪资

    # 展示员工基本信息的方法
    def show_info(self):
        print(f"员工姓名：{self.name}，员工年龄：{self.age}，员工薪资：{self.salary}")

    # 判断薪资水平的方法
    def judge_salary_level(self):
        # self.salary 获取当前对象的薪资属性
        if self.salary >= 10000:
            print(f"{self.name}薪资水平为高")
        elif self.salary >= 5000:
            print(f"{self.name}薪资水平中等")
        else:
            print(f"{self.name}薪资水平低")


# ----------------------------------------------------------------------
# 实习员工（子类），继承自 Staff
# 语法：class 子类名(父类名)
# ----------------------------------------------------------------------
class InternStaff(Staff):
    """
    实习员工类，继承 Staff 父类的所有属性和方法。
    只需要额外添加实习月数这一个独有属性。
    """

    def __init__(self, s_name, s_age, s_salary, intern_month):
        # super() 代表父类对象
        # super().__init__(...) 调用父类的构造方法，复用父类中公共属性的初始化逻辑
        # 这样就不需要再写一遍 self.name = s_name 等等
        super().__init__(s_name, s_age, s_salary)
        # 子类独有的属性：实习月数
        self.intern_month = intern_month

    # 子类独有的方法：展示实习信息
    def show_intern_info(self):
        print(
            f"实习员工姓名：{self.name}，"
            f"实习员工年龄：{self.age}，"
            f"实习员工薪资：{self.salary}，"
            f"实习月数：{self.intern_month}"
        )


# ----------------------------------------------------------------------
# 正式员工（子类），同样继承自 Staff
# ----------------------------------------------------------------------
class FormalStaff(Staff):
    """
    正式员工类，继承 Staff，并新增「津贴」属性。
    同时重写（override）父类的 judge_salary_level 方法，
    让薪资水平的判断包含津贴。
    """

    def __init__(self, s_name, s_age, s_salary, allowance):
        # 先初始化子类独有的属性
        self.allowance = allowance   # 津贴
        # 再调用父类构造方法，初始化公共属性
        super().__init__(s_name, s_age, s_salary)

    # 计算总收入（薪资 + 津贴）
    def get_info_Salay(self):
        info_Salay = self.salary + self.allowance
        return info_Salay

    # 方法重写（Override）：子类定义了一个和父类同名的方法
    # 调用时优先使用子类的版本，这就是「多态」
    def judge_salary_level(self):
        # 总收入 = 薪资 + 津贴
        total = self.salary + self.allowance
        if total >= 10000:
            return "高"
        elif total >= 5000:
            return "中等"
        else:
            return "低"

    # 展示正式员工的完整信息
    def show_formal_info(self):
        print(
            f"正式员工姓名：{self.name}，"
            f"正式员工年龄：{self.age}，"
            f"正式员工薪资：{self.salary}，"
            f"正式员工津贴：{self.allowance}，"
            f"正式员工总薪资：{self.get_info_Salay()}，"
            f"正式员工薪资水平：{self.judge_salary_level()}"
        )


# 测试：创建正式员工对象并展示信息
FormalStaff("张三", 30, 9000, 1000).show_formal_info()


# ======================================================================
# 二、学生继承示例：Student → littleStudent（小学生）
# ======================================================================

# 学生父类
class Student:
    """学生类，包含姓名、学号、自我介绍三个基本属性"""

    def __init__(self, name, id, introduction):
        self.name = name                 # 学生姓名
        self.id = id                     # 学号（id 是 Python 内置函数，通常不建议重名，这里仅作示例）
        self.introduction = introduction # 自我介绍

    # 展示学生个人信息
    def show_info(self):
        print(
            f"学生姓名：{self.name}，"
            f"学生id：{self.id}，"
            f"学生介绍：{self.introduction}"
        )


# 小学生子类
class littleStudent(Student):
    """小学生在学生基础上新增「年龄」属性"""

    def __init__(self, name, id, introduction, age):
        # 注意：这里先赋值了 self.name 和 self.age，
        # 然后又调用 super().__init__() 把 name 再赋值了一遍，是冗余写法。
        self.name = name
        self.age = age                  # 小学生独有属性：年龄
        super().__init__(name, id, introduction)

    # 方法重写：覆盖父类的 show_info
    def show_info(self):
        print(
            f"小学生姓名：{self.name}，"
            f"小学生年龄：{self.age}，"
            f"小学生介绍：{self.introduction}"
        )


# ======================================================================
# 三、宠物继承示例：Animal（动物） → Dog（狗）
# ======================================================================

# 宠物父类（动物）
class Animal:
    """动物父类，定义基本属性和叫声方法"""

    def __init__(self, name, species):
        self.name = name          # 名字
        self.species = species    # 品种（species = 物种）

    # 叫声方法
    def make_sound(self):
        print(f"{self.name}在叫")

    # 展示动物信息
    def show_info(self):
        print(f"动物姓名：{self.name}，动物品种：{self.species}")


# 狗子类
class Dog(Animal):
    """狗狗类，继承动物，新增毛色属性和看家方法"""

    def __init__(self, name, species, hair_color):
        super().__init__(name, species)   # 复用父类构造方法
        self.hair_color = hair_color      # 子类独有属性：毛色

    # 子类独有方法：看家
    def watch_home(self):
        print(f"{self.name}正在看家")

    # 方法重写：扩展父类的 show_info
    def show_info(self):
        print(
            f"动物姓名：{self.name}，"
            f"动物品种：{self.species}，"
            f"动物毛色：{self.hair_color}"
        )


# 测试：创建狗对象并展示信息
d = Dog("狗", "狗", "黄色")
d.show_info()


# ======================================================================
# 四、书籍继承示例：Book（书） → EBook（电子书）
# ======================================================================

# 书籍父类
class Book:
    """书籍类，包含书名和价格"""

    def __init__(self, title, price):
        self.title = title    # 书名（title = 标题）
        self.price = price    # 价格

    # 展示书籍信息
    def show_info(self):
        print(f"书名：{self.title}，价格：{self.price}")


# 电子书子类
class EBook(Book):
    """电子书类，继承书籍，新增文件格式属性"""

    def __init__(self, title, price, file_format):
        super().__init__(title, price)      # 复用父类构造方法
        self.file_format = file_format      # 子类独有属性：文件格式（如 PDF、EPUB）

    # 子类独有方法：打印文件格式
    def print_format(self):
        print(f"{self.title}的文件格式为：{self.file_format}")


# 测试：创建电子书对象并打印格式
e = EBook("Python从入门到精通", 100, "PDF")
e.print_format()


# ======================================================================
# 五、交通工具继承示例（含类型注解）
# ======================================================================

# ---------- 题目说明 ----------
# 定义交通工具父类（名称、速度、行驶方法）
# 定义汽车子类（新增座位数、鸣笛方法）
# 要求：使用类型注解（Type Hints）
# -------------------------------

class Vehicle:
    """
    交通工具父类。
    :param name: str  名称
    :param speed: int 速度
    类型注解写在参数后面，用冒号分隔，箭头 -> 后面是返回值类型。
    """

    # name: str  意思是 name 参数应该是字符串类型
    # speed: int 意思是 speed 参数应该是整数类型
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed

    # -> None 表示这个方法没有返回值
    def drive(self) -> None:
        """行驶方法"""
        print(f"{self.name}正在行驶，速度为{self.speed}")


# 汽车子类
class Car(Vehicle):
    """
    汽车类，继承交通工具。
    :param seats: int 座位数（子类独有属性）
    """

    def __init__(self, name: str, speed: int, seats: int):
        super().__init__(name, speed)   # 复用父类
        self.seats = seats              # 座位数（seats = 座位）

    def honk(self) -> None:
        """鸣笛方法（honk = 鸣笛/按喇叭）"""
        print(f"{self.name}正在鸣笛，速度为{self.speed}")
        print(f"{self.name}有{self.seats}个座位")


# 测试
Vehicle("飞机", 100).drive()
Car("奔驰", 200, 4).honk()


# ======================================================================
# 六、水果继承示例（含类型注解 + super() 调用父类方法）
# ======================================================================

# ---------- 题目说明 ----------
# 定义水果父类（名称、颜色、介绍方法）
# 定义苹果子类（新增产地、削皮方法）
# 要求：削皮方法中要先调用父类的介绍方法，再执行自己的削皮逻辑
# -------------------------------

class Fruit:
    """水果父类"""

    def __init__(self, name: str, color: str):
        self.name = name      # 水果名称
        self.color = color    # 水果颜色

    def show_info(self) -> None:
        """展示水果信息"""
        print(f"水果姓名：{self.name}，水果颜色：{self.color}")


class Apple(Fruit):
    """
    苹果子类，继承水果。
    :param origin: str 产地（origin = 来源/产地）
    """

    def __init__(self, name: str, color: str, origin: str):
        super().__init__(name, color)   # 调用父类构造方法
        self.origin = origin            # 子类独有属性：产地

    def peel(self) -> None:
        """削皮方法（peel = 削皮）"""
        # 先调用父类的 show_info() 展示基本信息
        super().show_info()
        # 再执行子类独有的削皮逻辑
        print(f"{self.name}正在削皮，产地为{self.origin}")


# 测试
Apple("苹果", "黄色", "中国").peel()


# ======================================================================
# 七、手机继承示例（含方法扩展 + 列表遍历）
# ======================================================================

# ---------- 题目说明 ----------
# 定义手机父类（品牌 brand、内存 storage）
# 定义游戏手机子类（新增散热类型 cooling、游戏模式、扩展打电话功能）
# -------------------------------

class Phone:
    """
    手机父类。
    :param brand:   str 品牌（brand = 品牌）
    :param storage: str 内存/存储空间（storage = 存储）
    """

    def __init__(self, brand: str, storage: str):
        self.brand = brand
        self.storage = storage

    def show_info(self) -> None:
        """展示手机信息"""
        print(f"手机品牌：{self.brand}，手机内存：{self.storage}")

    def call(self) -> None:
        """打电话方法"""
        print(f"{self.brand}正在打电话")


class GamePhone(Phone):
    """
    游戏手机子类，继承手机。
    :param cooling: str 散热类型（cooling = 冷却/散热）
    """

    def __init__(self, brand: str, storage: str, cooling: str):
        super().__init__(brand, storage)   # 复用父类
        self.cooling = cooling             # 散热类型（如：液冷、风冷）

    def show_info(self) -> None:
        """方法重写：先展示父类信息，再展示散热类型"""
        super().show_info()                # 调用父类的 show_info
        print(f"散热类型：{self.cooling}")

    def call(self) -> None:
        """方法重写：扩展打电话功能，增加感谢语"""
        super().call()                     # 先调用父类的打电话方法
        print("感谢你的接听")

    def start_game_mode(self) -> None:
        """子类独有方法：开启游戏模式"""
        print("开启游戏模式")


# 创建两个游戏手机对象
phone1 = GamePhone("荣耀", "256GB", "液冷")
phone2 = GamePhone("华为", "512GB", "风冷")

# 将手机对象放入列表
phone_list = [phone1, phone2]

# 遍历列表，对每个手机执行操作 —— 这就是「多态」：
# 同样的调用 phone()，不同的对象（普通Phone / 游戏Phone）表现不同
for i in phone_list:
    i.call()           # 打电话（如果是游戏手机还会输出感谢语）
    i.start_game_mode() # 开启游戏模式
    i.show_info()       # 展示信息


# ======================================================================
# 八、异步编程：async / await
# ======================================================================

import asyncio    # asyncio = Asynchronous I/O（异步 IO），Python 内置的异步编程库
import time       # time 模块，用于计时

# ---------- 异步函数（协程）----------
# async 关键字定义一个协程函数（coroutine）
# 协程：可以在执行过程中"暂停"并让出 CPU 给其他任务，等条件满足后再继续执行
async def my_func(name, delay):
    """
    异步任务函数。
    :param name:  str 任务名称
    :param delay: int 延迟时间（秒）
    :return:      str 任务结果字符串
    """
    print(f"任务 {name} 开始")

    # await = 等待
    # asyncio.sleep(delay) 是一个异步的"睡眠"，不会阻塞线程
    # 遇到 await 时，当前协程暂停，把控制权交还给事件循环，
    # 事件循环可以趁机去执行其他协程
    await asyncio.sleep(delay)

    print(f"任务 {name} 完成")
    return f"任务 {name} 结果"


# ---------- 串行执行示例 ----------
async def main_sync():
    """
    串行（同步）方式执行两个异步任务。
    虽然使用了 async/await，但因为是 await 一个接一个，
    总耗时 = A 的耗时 + B 的耗时。
    """
    print("--- 串行执行（总耗时 1s + 2s = 3s）---")
    # await 串行：必须等 A 完成，才会开始 B
    await my_func("A", 1)    # 等待 1 秒
    await my_func("B", 2)    # 等待 2 秒（串行总计 3 秒）


# ---------- 程序入口 ----------
# if __name__ == "__main__":  = 当这个文件被直接运行时（而不是被 import 时）才执行
if __name__ == "__main__":
    start_time = time.time()                    # 记录开始时间

    # asyncio.run() 启动事件循环，运行异步主函数
    asyncio.run(main_sync())

    # 计算并打印总耗时
    elapsed = time.time() - start_time
    print(f"串行耗时: {elapsed:.2f}秒")
    # 预期输出：串行耗时: 3.00秒