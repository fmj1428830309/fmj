# 4.4.4 在 main.py 中提供建表方法 + 4.4.5~4.4.8 增删改查

from datetime import date

from sqlalchemy import and_, or_, func
from sqlalchemy.orm import joinedload

from demo.base import Base
from demo.database import engine, SessionLocal
from demo.models import Employee, Department  # 必须要加


# 创建表结构（仅需执行一次）
def create_table():
    print("注册的表名:", Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)
    print("表创建成功")


# 4.4.5 新增数据（Create）
def insert_data():
    db = SessionLocal()
    try:
        # =========== 第一步：新增部门 =============
        new_dept = Department(
            name="研发部",
            location="北京总部"
        )
        db.add(new_dept)
        db.commit()
        db.refresh(new_dept)

        # =========== 第二步：新增关联的员工 ===========
        emp1 = Employee(name="张三", age=30, hire_date=date(2023, 1, 1), department_id=new_dept.id)
        emp2 = Employee(name="李四", age=28, hire_date=date(2023, 3, 15), department_id=new_dept.id)

        db.add_all([emp1, emp2])
        db.commit()
        db.refresh(emp1)
        db.refresh(emp2)

        print(f"新增部门：ID={new_dept.id}，名称={new_dept.name}，位置={new_dept.location}")
        print(f"新增员工1：ID={emp1.id}，姓名={emp1.name}，所属部门={new_dept.name}")
        print(f"新增员工2：ID={emp2.id}，姓名={emp2.name}，所属部门={new_dept.name}")

        # 验证关联关系
        print("\n【验证关联关系】")
        print(f"员工{emp1.name}的部门名称：{emp1.department.name}")
        dept_employees = new_dept.employees
        print(f"部门{new_dept.name}的员工列表：{[emp.name for emp in dept_employees]}")
    except Exception as e:
        db.rollback()
        print(f"新增失败：{e}")
    finally:
        db.close()


# 4.4.6 删除数据（Delete）
def delete_data():
    session = SessionLocal()
    try:
        emp = session.query(Employee).filter(Employee.name == "李四").first()
        if emp:
            session.delete(emp)
            session.commit()
            print(f"已删除员工：{emp.name}")
    except Exception as e:
        session.rollback()
        print(f"删除失败：{e}")
    finally:
        session.close()


# 4.4.7 修改数据（Update）
def update_data():
    session = SessionLocal()
    try:
        emp = session.query(Employee).filter(Employee.name == "张三").first()
        if emp:
            emp.age = 31
            session.commit()
            print(f"修改后 {emp.name} 的年龄：{emp.age}")
    except Exception as e:
        session.rollback()
        print(f"修改失败：{e}")
    finally:
        session.close()


# 4.4.8 查询数据（Read）
def read_data():
    session = SessionLocal()
    try:
        # 按主键查询 get
        dept = session.get(Department, 1)
        print(f"部门 ID=1：{dept.name}（{dept.location}）")

        # 过滤（filter）查询
        rd_employees = session.query(Employee).filter(Employee.department_id == 1).all()
        print("研发部员工：", [emp.name for emp in rd_employees])

        old_employees = session.query(Employee).filter(Employee.age > 30).all()
        print("年龄>30的员工：", [emp.name for emp in old_employees])

        # 逻辑运算（and_ / or_）
        emp = session.query(Employee).filter(
            and_(Employee.age.between(30, 40), Employee.department_id == 1)
        ).first()
        print("符合条件的员工：", emp.name)

        emps = session.query(Employee).filter(
            or_(Employee.department_id == 2, Employee.age > 32)
        ).all()
        print("符合条件的员工：", [emp.name for emp in emps])

        # 表连接（join）查询
        result = session.query(Employee, Department).join(
            Department, Employee.department_id == Department.id
        ).all()
        for emp, dept in result:
            print(f"员工 {emp.name} 属于 {dept.name}")

        # 预加载关联数据（joinedload）
        employees = session.query(Employee).options(joinedload(Employee.department)).all()
        for emp in employees:
            print(f"{emp.name} 的部门：{emp.department.name}")

        # 子查询（subquery）
        dept_emp_count = session.query(
            Employee.department_id,
            func.count(Employee.id).label("count")
        ).group_by(Employee.department_id).subquery()

        depts = session.query(Department).join(
            dept_emp_count, Department.id == dept_emp_count.c.department_id
        ).filter(dept_emp_count.c.count > 0).all()
        print("有员工的部门：", [dept.name for dept in depts])

        # 去重（distinct）
        locations = session.query(Department.location).join(Employee).distinct().all()
        print("部门位置：", [loc[0] for loc in locations])

        # 结果获取（first / all）
        first_emp = session.query(Employee).first()
        print("第一个员工：", first_emp.name)
        all_depts = session.query(Department).all()
        print("所有部门：", [dept.name for dept in all_depts])
    except Exception as e:
        session.rollback()
        print(f"查询失败：{e}")
    finally:
        session.close()


if __name__ == "__main__":
    # create_table()   # 首次执行：创建表
    # insert_data()    # 新增数据
    # delete_data()    # 删除数据
    # update_data()    # 修改数据
    # read_data()      # 查询数据
    pass
