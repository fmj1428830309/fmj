# -*- coding: utf-8 -*-
"""
数据模型层：只声明模型，不碰数据库连接、不碰 HTTP。

两类模型要分清：
    table=True 的  —— 映射真实数据库表（字段用 sa_column 指定真实列名）
    不带 table 的   —— 只描述请求体/响应体，不映射任何表
"""
from datetime import date
from decimal import Decimal
from typing import Annotated, Any, Generic, Literal, Optional, TypeVar

from pydantic import BaseModel, ConfigDict
from pydantic import Field as PydanticField  # 别名，避免和 sqlmodel 的 Field 撞名
from sqlalchemy import CHAR, Column, Date, DECIMAL, Enum, Integer, String
from sqlmodel import Field, SQLModel

# 泛型参数：T 代表 data 里装的具体类型，使用时才确定
T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """
    FastAPI 统一返回格式，方便前端一套逻辑解析所有接口。

    关键是用【泛型】而不是把 data 写成 Any：
        data: Any                  → Swagger 里 data 只显示成 {}，前端看不到字段
        data: Optional[T]          → 声明 ApiResponse[Employee] 后，文档里能看到完整结构

    用法：
        response_model=ApiResponse[Employee]
        response_model=ApiResponse[list[Employee]]
        return ApiResponse(data=employee)
    """

    # code 不需要 Optional —— 成功失败都会有值，给个默认 200
    code: int = 200
    msg: str = "操作成功"
    # data 默认 None，允许为空的接口（比如删除）直接用
    data: Optional[T] = None


# # ==================== Department（映射 t_department）====================
# # 真实表结构：部门编号(PK) / 部门名称 / 部门简介 —— 全是中文列名
# class DepartmentBase(SQLModel):
#     """部门的基础字段（不映射表，字段名可以自由用英文）"""
#     name: str
#     description: str
#
#
# class DepartmentCreate(DepartmentBase):
#     """新增部门时的请求体"""
#     pass
#
#
# class DepartmentRead(DepartmentBase):
#     """查询部门时的响应体"""
#     id: int
#
#
# class Department(DepartmentBase, table=True):
#     """映射真实表；字段在子类里用 sa_column 覆盖成中文列名"""
#     __tablename__ = "t_department"
#
#     id: Optional[int] = Field(
#         default=None,
#         sa_column=Column("部门编号", Integer, primary_key=True, autoincrement=True),
#     )
#     name: str = Field(sa_column=Column("部门名称", String(20), nullable=False))
#     description: str = Field(sa_column=Column("部门简介", String(20), nullable=False))


# ==================== Employee（映射 t_employee）====================
class Employee(SQLModel, table=True):
    """映射到已有的中文列名表 t_employee"""

    __tablename__ = "t_employee"

    # 主键：旧表列名是「员工编号」
    id: Optional[int] = Field(
        default=None,
        sa_column=Column("员工编号", Integer, primary_key=True, autoincrement=True),
    )
    name: str = Field(sa_column=Column("姓名", String(20), nullable=False))
    salary: Decimal = Field(sa_column=Column("薪资", DECIMAL(10, 2), nullable=False))
    bonus_pct: Optional[Decimal] = Field(
        default=None, sa_column=Column("奖金比例", DECIMAL(5, 2), nullable=True)
    )
    birth_date: date = Field(sa_column=Column("出生日期", Date, nullable=False))
    # 性别在库里是 ENUM('男','女')。注解用 Literal 而不是 str，
    # 传 "string" 这类非法值会在校验阶段直接 422，不会打到数据库。
    gender: Literal["男", "女"] = Field(
        sa_column=Column("性别", Enum("男", "女", name="gender_enum"), nullable=False)
    )
    telephone: str = Field(sa_column=Column("手机号码", CHAR(11), nullable=False))
    email: str = Field(sa_column=Column("邮箱", String(30), nullable=False))
    address: str = Field(sa_column=Column("地址", String(20), nullable=False))
    work_location: str = Field(sa_column=Column("工作地点", String(30), nullable=False))
    hire_date: date = Field(sa_column=Column("入职日期", Date, nullable=False))
    # 下面三个外键列：约束在数据库里已经存在，ORM 这边只当普通列用。
    # 如果写 ForeignKey("t_job.职位编号")，那 t_job 也必须在本文件的
    # metadata 里定义，否则 SQLAlchemy 建映射时会抛 NoReferencedTableError。
    job_id: Optional[int] = Field(
        default=None, sa_column=Column("职位编号", Integer, nullable=True)
    )
    manager_id: Optional[int] = Field(
        default=None, sa_column=Column("领导编号", Integer, nullable=True)
    )
    dept_id: Optional[int] = Field(
        default=None, sa_column=Column("部门编号", Integer, nullable=True)
    )


# 数据库里「薪资」是 DECIMAL(10, 2) —— 8 位整数 + 2 位小数，上限 99999999.99
MAX_SALARY = Decimal("99999999.99")

# ---------------- 正则校验规则（统一在这里维护） ----------------
# ⚠️ 这些规则必须写在【非 table】的请求体模型（EmployeeCreate / EmployeePatch）上才生效。
#    写在 Employee（table=True）上是没用的 —— SQLModel 不跑那一层的 pydantic 校验。
NAME_RE = r"^[\u4e00-\u9fa5·]{2,20}$"        # 中文姓名 2~20 字（允许「·」用于少数民族姓名）
PHONE_RE = r"^1[3-9]\d{9}$"                  # 大陆手机号：1 开头、第 2 位 3~9、共 11 位
EMAIL_RE = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"   # 常规邮箱格式

# 校验规则做成「类型别名」：
# ⚠️ 不能用 sqlmodel 的 Field(pattern=...) —— 它不支持 pattern 关键字（只认自己白名单里的参数），
#    会直接抛 TypeError: Field() got an unexpected keyword argument 'pattern'。
#    所以借 pydantic 的 Field，通过 Annotated 把规则绑到类型上；两个请求体模型都能复用。
NameStr = Annotated[str, PydanticField(min_length=2, max_length=20, pattern=NAME_RE)]
PhoneStr = Annotated[str, PydanticField(pattern=PHONE_RE)]
EmailStr = Annotated[str, PydanticField(max_length=30, pattern=EMAIL_RE)]


class EmployeeCreate(SQLModel):
    """
    POST /employees 的请求体。
Us
    为什么不直接拿 Employee（table 模型）当请求体？
    因为 SQLModel 的 table 模型在 FastAPI 里【不跑 pydantic 校验】——
    实测：field_validator 不执行、连字符串都不会转成 Decimal，
    非法数据会一路带进数据库，最后变成一个看不懂的 400
    （比如 MySQL 1264 "Out of range value for column '薪资'"）。
    所以新增也要像 PATCH 那样，用专门的非 table 模型来收请求体。
    """

    model_config = ConfigDict(extra="forbid")

    name: NameStr
    # 上限跟数据库 DECIMAL(10, 2) 对齐，超了在校验阶段直接 422
    salary: Decimal = Field(ge=0, le=MAX_SALARY)
    # 奖金比例是小数（0.67 = 67%）；如果你们习惯用「20 表示 20%」的整数写法，
    # 把 le 改成 999.99（那才是 DECIMAL(5,2) 的真实上限）
    bonus_pct: Optional[Decimal] = Field(default=None, ge=0, le=1)
    birth_date: date
    gender: Literal["男", "女"]
    telephone: PhoneStr
    email: EmailStr
    address: str
    work_location: str
    hire_date: date
    job_id: Optional[int] = None
    manager_id: Optional[int] = None
    dept_id: Optional[int] = None


class EmployeePatch(SQLModel):
    """
    PATCH 请求体：全部字段可选，只写要改的那个。
    不加 table=True —— 它只描述请求体，不映射任何表。
    """

    # extra="forbid"：请求体里出现不认识的字段，直接 422 报错。
    # 不加这一行，pydantic 默认是「静默忽略」—— 字段名拼错了会毫无提示地什么都没改，
    # 这种 bug 最难查。（用裸 dict 当 请求体时反而能看到「未知字段」提示，这里要补回来。）
    model_config = ConfigDict(extra="forbid")

    name: Optional[NameStr] = None
    salary: Optional[Decimal] = Field(default=None, ge=0, le=MAX_SALARY)
    bonus_pct: Optional[Decimal] = Field(default=None, ge=0, le=1)
    birth_date: Optional[date] = None
    gender: Optional[Literal["男", "女"]] = None
    telephone: Optional[PhoneStr] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    work_location: Optional[str] = None
    hire_date: Optional[date] = None
    job_id: Optional[int] = None
    manager_id: Optional[int] = None
    dept_id: Optional[int] = None


# ==================== 部门 ====================
# t_department 的列名本身就是中文：部门编号 / 部门名称 / 部门简介
class Department(SQLModel, table=True):
    """映射到已有的中文列名表 t_department"""

    __tablename__ = "t_department"

    id: Optional[int] = Field(
        default=None,
        sa_column=Column("部门编号", Integer, primary_key=True, autoincrement=True),
    )
    name: str = Field(sa_column=Column("部门名称", String(20), nullable=False))
    # 前端页面用的字段名叫 description，这里保持一致，列还是「部门简介」
    description: str = Field(sa_column=Column("部门简介", String(20), nullable=False))


# 两列都是 varchar(20) 且 NOT NULL，长度卡 1~20
DeptStr = Annotated[str, PydanticField(min_length=1, max_length=20)]


class DepartmentCreate(SQLModel):
    """POST /department 的请求体。description 对应页面上的「部门简介」。"""

    model_config = ConfigDict(extra="forbid")

    name: DeptStr
    description: DeptStr
