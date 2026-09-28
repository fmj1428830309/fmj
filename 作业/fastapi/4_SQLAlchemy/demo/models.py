# 4.4.2 在 models.py 中定义 ORM 模型类（映射 MySQL 表）
# 模型类需继承 Base 基类，类属性对应表字段

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from demo.base import Base


class Department(Base):
    """部门模型（一对多：一个部门包含多个员工）"""
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)  # 部门名称
    location = Column(String(100))  # 部门位置（如"北京总部"）

    # 一对多关联员工：返回员工列表，显式指定外键（可选，但更清晰）
    employees = relationship(
        "Employee",
        back_populates="department",
        lazy="selectin"
    )


class Employee(Base):
    """员工模型（多对一：多个员工属于一个部门）"""
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)  # 姓名
    age = Column(Integer)  # 年龄
    hire_date = Column(Date)  # 入职日期

    # 添加外键约束，绑定到 departments.id
    department_id = Column(
        Integer,
        ForeignKey("departments.id", ondelete="RESTRICT"),  # 禁止删除有员工的部门
        nullable=False  # 员工必须归属一个部门
    )

    # 多对一关联，指定 uselist=False（返回单个部门对象）
    department = relationship(
        "Department",
        back_populates="employees",
        lazy="joined"  # 立即加载部门数据，减少查询次数
    )
