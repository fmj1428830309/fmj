from typing import TypeVar
from pydantic import BaseModel, ConfigDict
from datetime import date
from decimal import Decimal
from typing import Annotated, Any, Generic, Literal, Optional, TypeVar
from sqlalchemy import CHAR, Column, Date, DECIMAL, Enum, Integer, String
from sqlmodel import SQLModel, Field

from pydantic import Field as PydanticField  # 别名，避免和 sqlmodel 的 Field 撞名
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


class User(SQLModel, table=True):
    """
    映射已存在的旧表 t_user —— 列名必须和数据库里的真实列名一致，
    之前写成中文列名（而且 age 那行还误写成 Column("性别")），
    SQLAlchemy 会直接报 "specifies more than one column named 性别"。
    """
    __tablename__ = "t_user"
    id: Optional[int] = Field(
        default=None,
        sa_column=Column("id", Integer, primary_key=True, autoincrement=True),
    )
    name: str = Field(sa_column=Column("name", String(50), nullable=False))
    age: Optional[int] = Field(
        default=None, sa_column=Column("age", Integer, nullable=True)
    )
    sex: Literal["男", "女"] = Field(
        sa_column=Column("sex", Enum("男", "女", name="gender_enum"), nullable=True)
    )
    telephone: str = Field(sa_column=Column("telephone", CHAR(11), nullable=True))
    email: str = Field(sa_column=Column("email", String(100), nullable=True))

NAME_RE = r"^[\u4e00-\u9fa5·]{2,20}$"        # 中文姓名 2~20 字（允许「·」用于少数民族姓名）
PHONE_RE = r"^1[3-9]\d{9}$"                  # 大陆手机号：1 开头、第 2 位 3~9、共 11 位
EMAIL_RE = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"   # 常规邮箱格式
AGE_RE = r"^[0-9]{1,2}$"
NameStr = Annotated[str, PydanticField(min_length=2, max_length=20, pattern=NAME_RE)]
PhoneStr = Annotated[str, PydanticField(pattern=PHONE_RE)]
EmailStr = Annotated[str, PydanticField(max_length=30, pattern=EMAIL_RE)]
AGEStr = Annotated[str, PydanticField(max_length=20, pattern=AGE_RE)]

# 年龄范围卡死在这一处：ge=0 挡负数，le=150 挡离谱值。新增和局部更新共用这一个别名。
AgeInt = Annotated[int, PydanticField(ge=0, le=150)]


class UserCreate(SQLModel):
    """新增用户的请求体。注意：这不是表！写 table=True 会凭空多建一张 usercreate 表。"""
    model_config = ConfigDict(extra="forbid")
    name: NameStr
    age: AgeInt
    sex: Literal["男", "女"]
    telephone: PhoneStr
    email: EmailStr


class UserPatch(SQLModel):
    model_config = ConfigDict(extra="forbid")
    name: Optional[NameStr] = None
    sex: Optional[Literal["男", "女"]] = None
    telephone: Optional[PhoneStr] = None
    email: Optional[EmailStr] = None
    age: Optional[AgeInt] = None