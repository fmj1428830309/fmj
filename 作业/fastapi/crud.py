# -*- coding: utf-8 -*-
"""
CRUD 层：只操心「数据库该怎么改」，不创建 Session、也不管理连接生命周期。
Session 由调用方（路由层）注入进来。
"""
from fastapi import HTTPException
from sqlalchemy.exc import DataError, IntegrityError
from sqlmodel import Session, select

from models import Department, DepartmentCreate, Employee, EmployeeCreate, EmployeePatch


def list_employees(session: Session) -> list[Employee]:
    """查询全部"""
    return session.exec(select(Employee)).all()


def read_employee(session: Session, employee_id: int) -> Employee:
    """按编号查一个；不存在直接 404，供下面几个函数复用"""
    employee = session.get(Employee, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="员工不存在")
    return employee


def search_employees_by_name(session: Session, name: str) -> list[Employee]:
    """姓名没有唯一约束，可能重名，所以返回列表"""
    return session.exec(select(Employee).where(Employee.name == name)).all()


def create_employee(session: Session, data: EmployeeCreate) -> Employee:
    """
    新增：id 交给数据库自增。

    注意入参是 EmployeeCreate（非 table 的请求体模型），不是 Employee（表模型）——
    这样字段类型和数值范围在进到这一层之前就已经校验过了。
    """
    employee = Employee(**data.model_dump())  # 请求体模型 → 表模型
    employee.id = None  # 客户端就算传了 id 也不认
    session.add(employee)
    try:
        session.commit()
    except (IntegrityError, DataError) as e:
        session.rollback()
        # ⚠️ 不要把原始异常拼进 detail：那会把整条 SQL 语句和所有参数
        # （表名、列名、业务数据）原样返回给客户端，属于信息泄露。
        # 详细信息只打服务端日志，客户端看到的是一句友好提示。
        print(f"[create_employee] 数据库错误: {e}")
        raise HTTPException(
            status_code=400,
            detail="插入失败：数据不合法，或关联的职位/领导/部门不存在",
        )
    session.refresh(employee)
    return employee


def update_employee(
    session: Session, employee_id: int, patch: EmployeePatch
) -> Employee:
    """
    局部更新：只改请求体里出现过的字段。

    exclude_unset=True 才分得清「没传」（保持原值）和「传了 null」（把列清成 NULL），
    换成 exclude_none 的话传 null 会被当成没传，清空功能就废了。
    """
    data = patch.model_dump(exclude_unset=True)
    if not data:
        raise HTTPException(status_code=400, detail="没有需要更新的字段")

    employee = read_employee(session, employee_id)  # 不存在会抛 404
    for field, value in data.items():
        setattr(employee, field, value)
    try:
        session.commit()
    except (IntegrityError, DataError) as e:
        session.rollback()
        print(f"[update_employee] 数据库错误: {e}")
        raise HTTPException(
            status_code=400,
            detail="更新失败：数据不合法，或关联的职位/领导/部门不存在",
        )
    session.refresh(employee)
    return employee


def remove_employee(session: Session, employee_id: int) -> dict:
    """删除：先确认存在，避免「删了个不存在的 id」也返回成功"""
    employee = read_employee(session, employee_id)  # 不存在会抛 404
    session.delete(employee)
    session.commit()
    return {"message": "员工删除成功"}


# ==================== 部门 ====================
def list_departments(session: Session) -> list[Department]:
    """查询全部部门"""
    return session.exec(select(Department).order_by(Department.id)).all()


def read_department(session: Session, department_id: int) -> Department:
    """按编号查一个；不存在直接 404"""
    department = session.get(Department, department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="部门不存在")
    return department


def create_department(session: Session, data: DepartmentCreate) -> Department:
    """新增部门：name / description 都必填，长度 1~20 在请求体层已经校验过"""
    department = Department(**data.model_dump())
    department.id = None  # 客户端就算传了 id 也不认
    session.add(department)
    try:
        session.commit()
    except (IntegrityError, DataError) as e:
        session.rollback()
        print(f"[create_department] 数据库错误: {e}")
        raise HTTPException(status_code=400, detail="插入失败：部门名称或简介不合法")
    session.refresh(department)
    return department


def remove_department(session: Session, department_id: int) -> dict:
    """
    删除部门。
    t_employee.部门编号 外键指向 t_department.部门编号 —— 部门下还有员工时
    数据库会拒绝删除（IntegrityError），这里翻译成一句人话提示。
    """
    department = read_department(session, department_id)  # 不存在会抛 404
    session.delete(department)
    try:
        session.commit()
    except IntegrityError as e:
        session.rollback()
        print(f"[remove_department] 数据库错误: {e}")
        raise HTTPException(
            status_code=400,
            detail="删除失败：该部门下还有员工，请先删除或转移这些员工",
        )
    return {"message": "部门删除成功"}
