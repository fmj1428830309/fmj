from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine
from sqlmodel import Session, create_engine
# charset=utf8mb4 必须带上！少了它，中文列名和中文数据都会乱码。
DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3306/a_my_store?charset=utf8mb4"

engine = create_engine(
    DATABASE_URL,
    echo=False,  # 调试时改 True，会把每条 SQL 都打印出来
)

# 【不要】在这里写 SQLModel.metadata.create_all(engine)
# a_my_store 里的表都是别人早就建好的旧表，ORM 只负责「映射」，不负责「建表」。
# 只有当你自己从零设计表结构时，才需要 create_all。


def get_session():
    """
    FastAPI 的 yield 依赖：每个请求开一个 Session，请求结束后自动关闭。
    yield 之前是准备工作，yield 之后（哪怕抛异常）是清理工作。
    """
    with Session(engine) as session:
        yield session


# 把「Session 类型 + 怎么拿到它」打包成一个别名，
# 路由签名里直接写 session: SessionDep 就行，不用每次重复 Depends。
SessionDep = Annotated[Session, Depends(get_session)]