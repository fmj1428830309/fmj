# 3.6.2.3 商品模块路由定义（routers/item.py）

from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["商品管理"]  # 文档中归类为「商品管理」
)


# 定义商品相关路由
@router.get("/")
def get_all_items():
    return {"message": "获取所有商品列表"}


@router.get("/{item_id}")
def get_item(item_id: int):
    return {"message": f"获取 ID 为 {item_id} 的商品信息"}
