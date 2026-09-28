from datetime import datetime

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    counter = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.counter += 1
        self.std_id = f"{datetime.now().year}{Student.counter:03d}"
        self.score = {}

    def add_score(self, course, score):
        self.score[course] = score

    def average_score(self):
        if not self.score:
            return 0.0
        return sum(self.score.values()) / len(self.score)

    def __str__(self):
        return (
            f"学号: {self.std_id}, 姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}, "
            f"平均成绩: {self.average_score():.2f}"
        )


class Manager:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input('请输入学生姓名：').strip()
        if not name:
            print('姓名不能为空')
            return
        try:
            age = int(input('请输入学生年龄：'))
        except ValueError:
            print('年龄必须为整数')
            return
        gender = input('请输入学生性别：').strip()
        s = Student(name, age, gender)
        self.students.append(s)
        print(f'学生 {s.name} 添加成功，学号为 {s.std_id}')

    def remove_student(self):
        std_id = input('请输入要删除的学生学号：').strip()
        for s in self.students:
            if s.std_id == std_id:
                self.students.remove(s)
                print(f'学生 {s.name} 删除成功')
                return True
        print('未找到该学生')
        return False

    def find_student(self, std_id):
        for s in self.students:
            if s.std_id == std_id:
                return s
        return None

    def show_all_students(self):
        if not self.students:
            print('没有学生信息')
        else:
            print('所有学生信息如下：')
            for s in self.students:
                print(s)

    def add_score_to_student(self):
        std_id = input('请输入要添加成绩的学生学号：').strip()
        s = self.find_student(std_id)
        if s:
            course = input('请输入课程名称：').strip()
            try:
                score = float(input('请输入课程成绩：'))
            except ValueError:
                print('成绩必须为数字')
                return
            s.add_score(course, score)
            print(f'已为学生 {s.name} 添加课程 {course} 的成绩 {score}')
        else:
            print('未找到该学生')

    def run(self):
        while True:
            print('欢迎使用学生管理系统')
            print('1. 添加学生')
            print('2. 删除学生')
            print('3. 查询学生')
            print('4. 显示所有学生信息')
            print('5. 给指定学生添加成绩')
            print('0. 退出系统')
            choice = input('请输入操作编号：').strip()
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.remove_student()
            elif choice == '3':
                std_id = input('请输入要查询的学生学号：').strip()
                s = self.find_student(std_id)
                if s:
                    print(s)
                else:
                    print('未找到该学生')
            elif choice == '4':
                self.show_all_students()
            elif choice == '5':
                self.add_score_to_student()
            elif choice == '0':
                print('退出系统')
                break
            else:
                print('无效的操作编号，请重新输入')


if __name__ == '__main__':
    M1 = Manager()
    M1.run()