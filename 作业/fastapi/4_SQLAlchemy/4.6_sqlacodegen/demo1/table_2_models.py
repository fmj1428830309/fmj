# 4.6.4 提示：本文件用于接收 sqlacodegen 生成的模型类
# 运行 gen.py 中的 table_2_model(True) 后，
# 会自动把 Departments / Employees 模型类写入本文件。

# 下面是 sqlacodegen 生成后的预期结构（示意，实际以生成为准）：

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Departments(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    location = Column(String(100))
    created_at = Column(DateTime)


class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    hire_date = Column(Date)
    department_id = Column(ForeignKey('departments.id'))
