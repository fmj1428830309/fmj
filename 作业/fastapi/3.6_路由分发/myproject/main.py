# 3.6 路由分发
# 项目结构：
# myproject/
# ├── main.py          # 主应用
# └── routers/
#     ├── user.py       # 用户相关路由
#     └── item.py       # 商品相关路由

from fastapi import FastAPI
from routers import user, item  # 导入子模块路由
import uvicorn

app = FastAPI(title="路由分发示例")

# 挂载用户路由：所有 /users 开头的请求由 user.router 处理
app.include_router(user.router)

# 挂载商品路由：所有 /items 开头的请求由 item.router 处理
app.include_router(item.router)


# 主应用自身也可以定义路由
@app.get("/")
def root():
    return {"message": "欢迎访问主页面"}


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=False
    )
