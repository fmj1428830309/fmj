# 3.4 请求参数（查询参数）
# 声明的参数不是路径参数时，自动解释为查询参数，按参数名字匹配

from fastapi import FastAPI
import uvicorn

app = FastAPI()

items_list = [{"item1": "Foo"}, {"item2": "Bar"}, {"item3": "Baz"}]


# 3.4.1 案例 + 3.4.2 默认值：start=0、limit=10 为默认值
@app.get("/items/")
async def read_item(start: int = 0, limit: int = 10):
    return items_list[start: start + limit]


# 3.4.3 可选参数：默认值设为 None 即声明可选查询参数
@app.get("/items/{item_id}")
async def read_item_optional(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# 3.4.4 查询参数类型转换：bool 类型自动转换
# short=1|True|true|on|yes（任意大小写）都会转为 True
@app.get("/items2/{item_id}")
async def read_item_bool(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "这是描述信息"})
    return item


# 3.4.5 多个路径参数和查询参数：声明顺序不重要，FastAPI 按参数名检测
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "这是描述信息"})
    return item


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
