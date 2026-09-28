# 第5章 数据库配置（引擎、会话），复用第四章的 database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/a_my_store"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    bind=engine
)
# 把「Session 类型 + 怎么拿到它」打包成一个别名，
# 路由签名里直接写 session: SessionDep 就行，不用每次重复 Depends。
SessionDep = Annotated[Session, Depends(get_session)]