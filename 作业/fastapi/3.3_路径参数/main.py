# 3.3 路径参数
# FastAPI 支持使用 Python 字符串格式化语法声明路径参数（变量）

from fastapi import FastAPI
import uvicorn

app = FastAPI()


# 3.3.1 案例：把路径参数 item_id 的值传给路径函数的参数 item_id
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# 3.3.2 声明路径参数的类型以及类型转换
# 使用类型注解声明参数类型，FastAPI 会自动将字符串 "3" 转换为 int 3
@app.get("/items2/{item_id}")
async def read_item_typed(item_id: int):
    return {"item_id": item_id}


# 3.3.4 参数顺序：
# 路径操作按顺序依次运行，必须先声明 /users/me，再声明 /users/{user_id}
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
