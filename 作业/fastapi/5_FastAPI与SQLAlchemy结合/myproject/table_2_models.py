# 第5章 SQLAlchemy 模型（映射 MySQL 表），复用第四章的 table_2_models.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Departments(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    location = Column(String(100))



class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    hire_date = Column(Date)
    department_id = Column(ForeignKey('departments.id'))
