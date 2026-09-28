# 4.4.1 在 接口.py 中定义 Base 基类

from sqlalchemy.ext.declarative import declarative_base

# 生成基类，所有模型需继承该类
Base = declarative_base()
