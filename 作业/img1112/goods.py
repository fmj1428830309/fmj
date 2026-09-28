from typing import Optional

from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select
from starlette.staticfiles import StaticFiles

app = FastAPI()
class Goods(SQLModel, table=True):
    __tablename__ = "goods"
    __table_args__ = {"extend_existing": True}
    # 2. id：int，主键，自增，默认值 None
    goods_id: Optional[int] = Field(default=None, primary_key=True)
    # 3. title：字符串，最大长度 50，必填
    title: str = Field(max_length=50)  # 必填，最大50字符
    # 4. price：float，必填，价格≥0
    price: float = Field(ge=0)  # 必填，价格≥0
    # 5. stock：int，必填，库存≥0
    stock: int = Field(ge=0)
# ==================== 数据库配置 ====================
engine = create_engine(
    "mysql+pymysql://root:203227944fmj@127.0.0.1:3306/mytest01",
    echo=True
)
# ==================== 新增 ====================
@app.post("/goods")
def add_goods(goods: Goods):
    with Session(engine) as session:
        session.add(goods)
        session.commit()
        session.refresh(goods)
        return goods
@app.put("/goods/{goods_id}")
def update_goods(goods_id: int, goods: Goods):
    with Session(engine) as session:
        db_goods = session.get(Goods, goods_id)
        if db_goods is None:
            return {"message": "商品不存在"}
        db_goods.title = goods.title  # 从参数取字段更新到数据库记录
        db_goods.price = goods.price
        db_goods.stock = goods.stock
        session.commit()
        session.refresh(db_goods)
        return db_goods
@app.delete("/goods/{goods_id}")
def delete_goods(goods_id: int):
    with Session(engine) as session:
        db_goods = session.get(Goods, goods_id)
        if db_goods is None:
            return {"message": "商品不存在"}
        session.delete(db_goods)
        session.commit()
        return {"message": "商品删除成功"}
#
# # ==================== 查询全部 ====================
@app.get("/goods")
def get_list():
    with Session(engine) as session:
        statement = select(Goods)
        goods_list = session.exec(statement).all()
        return goods_list

#
# # ==================== 根据 ID 查询（修正版）====================
@app.get("/goods/{goods_id}")
def get_goods_by_id(goods_id: int):
    with Session(engine) as session:
        statement = select(Goods).where(Goods.goods_id == goods_id)
        goods = session.exec(statement).first()
        return goods
# ==================== 主程序 ====================
# if __name__ == "__main__":
    # add_goods(Goods(title="苹果", price=3, stock=30))
    # #
    # # # 测试：查询全部
    # print(get_all_goods())
    # # # #
    # # # # # 测试：根据 ID 查询
    # print(get_goods_by_id(10))
    # # # # #
    # # # # # # 测试：修改
    # # # 函数保持 goods: Goods 不变
    # print(update_goods(6, Goods(title="冰箱", price=10000, stock=11)))
    #
    # # #
    # # # # 测试：删除
    # print(delete_goods(16))
from pathlib import Path
STATIC_DIR = Path(__file__).parent
STATIC_DIR.mkdir(exist_ok=True)
app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="img1112")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("goods:app", host="0.0.0.0", port=8085, reload=True)
