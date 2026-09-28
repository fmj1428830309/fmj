# 3.5 请求体传参数
# FastAPI 使用请求体从客户端向 API 发送数据，使用 Pydantic 模型声明请求体
# 发送数据使用 POST（最常用）、PUT、DELETE、PATCH 等操作

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


# 定义数据模型类，需继承 BaseModel
class Item(BaseModel):
    name: str
    desc: str | None = None
    price: float


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
