# 4.5 关联关系（Relationship）
# 定义不同模型（表）之间的业务关联：一对一、一对多、多对多

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


# ============ 4.5.3.1 一对多 / 多对一（用户-商品） ============
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))

    # 一对多：用户拥有多个商品（back_populates 与 Item.owner 双向关联）
    items = relationship(
        "Item",
        back_populates="owner",
        lazy="selectin",
        cascade="save-update"
    )


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    owner_id = Column(Integer, ForeignKey("users.id"))

    # 多对一：商品属于一个用户（反向关联）
    owner = relationship("User", back_populates="items")


# ============ 4.5.3.2 一对一（用户-个人资料） ============
class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    bio = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)  # 外键唯一

    user = relationship("User", back_populates="profile")


# 补充 User 的一对一关联（实际使用中应写在 User 类里）
User.profile = relationship(
    "Profile",
    back_populates="user",
    uselist=False,
    cascade="all, delete-orphan"
)


# ============ 4.5.3.3 多对多（学生-课程） ============
# 定义中间表（无需模型类，直接用 Table 定义）
student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True)
)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates="students",
        lazy="selectin"
    )


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    students = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses"
    )


if __name__ == "__main__":
    print("关联关系模型已定义")
    print("一对多：User.items <-> Item.owner")
    print("一对一：User.profile <-> Profile.user（uselist=False）")
    print("多对多：Student.courses <-> Course.students（中间表 student_course）")
