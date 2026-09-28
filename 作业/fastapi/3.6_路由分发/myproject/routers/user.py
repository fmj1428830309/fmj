# 3.6.2.2 用户模块路由定义（routers/user.py）

from fastapi import APIRouter

# 实例化一个 APIRouter，可指定前缀（所有路由自动加上 /users）
router = APIRouter(
    prefix="/users",
    tags=["用户管理"]  # 文档中归类为「用户管理」
)


# 定义用户相关路由
@router.get("/")
def get_all_users():
    return {"message": "获取所有用户列表"}


@router.get("/{user_id}")
def get_user(user_id: int):
    return {"message": f"获取 ID 为 {user_id} 的用户信息"}
