# -*- coding: utf-8 -*-
"""
pymysql 操作商品表 t_goods 的 CRUD 案例
前置条件：库里要有 t_category（分类表）和 t_goods（商品表）
          shopping 和 a_my_store 两个库现在都有这两张表，DB_CONFIG 里选一个即可
依赖安装：pip install pymysql
"""

import pymysql
from pymysql.cursors import DictCursor

# ==================== 数据库配置（跟你作业里 database.py 的写法对齐） ====================
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456",   # ← 换成你自己的 MySQL 密码
    # t_category / t_goods 现在 shopping 和 a_my_store 两个库里都有（结构和数据一致）
    # 想换库就改这一行：a_my_store 或 shopping
    "database": "a_my_store",
    "charset": "utf8mb4",
    "cursorclass": DictCursor,    # 查询结果直接返回字典，不用记下标
    "autocommit": False,          # 手动提交，出错能回滚
}


def get_conn():
    """获取一个数据库连接"""
    return pymysql.connect(**DB_CONFIG)


# ==================== C：新增 ====================
def add_goods(goods_name, price, stock, produce_date, is_sale=1, cat_id=None):
    """新增商品，返回新记录的自增 good_id"""
    sql = """
        INSERT INTO t_goods (goods_name, price, stock, produce_date, is_sale, cat_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # 一律用 %s 占位符传参，千万别用 f-string 拼 SQL（会被注入）
            cur.execute(sql, (goods_name, price, stock, produce_date, is_sale, cat_id))
            new_id = cur.lastrowid
        conn.commit()          # 写操作必须提交
        return new_id
    except Exception:
        conn.rollback()        # 出错回滚
        raise
    finally:
        conn.close()           # 用完一定关连接


# ==================== R：查询 ====================
def get_goods_list(keyword=None, only_on_sale=False):
    """查询商品列表；keyword 按名称模糊匹配，only_on_sale 只看上架的"""
    sql = "SELECT * FROM t_goods WHERE 1 = 1"
    args = []
    if keyword:
        sql += " AND goods_name LIKE %s"
        args.append(f"%{keyword}%")
    if only_on_sale:
        sql += " AND is_sale = %s"
        args.append(1)
    sql += " ORDER BY price DESC"

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, args)
            return cur.fetchall()      # 多条
    finally:
        conn.close()


def get_goods_by_id(good_id):
    """按主键查单条，查不到返回 None"""
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM t_goods WHERE good_id = %s", (good_id,))
            return cur.fetchone()      # 单条
    finally:
        conn.close()


# ==================== U：更新 ====================
def update_goods(good_id, price=None, stock=None, is_sale=None):
    """按主键更新，只传要改的字段；返回受影响行数"""
    fields, args = [], []
    if price is not None:
        fields.append("price = %s")
        args.append(price)
    if stock is not None:
        fields.append("stock = %s")
        args.append(stock)
    if is_sale is not None:
        fields.append("is_sale = %s")
        args.append(is_sale)
    if not fields:
        return 0

    # 字段名来自上面固定的白名单，不是用户输入；值仍然全部走 %s
    sql = f"UPDATE t_goods SET {', '.join(fields)} WHERE good_id = %s"
    args.append(good_id)

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, args)
            rows = cur.rowcount
        conn.commit()
        return rows
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


# ==================== D：删除 ====================
def delete_goods(good_id):
    """按主键删除；返回受影响行数"""
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM t_goods WHERE good_id = %s", (good_id,))
            rows = cur.rowcount
        conn.commit()
        return rows
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


# ==================== 自测：跑一遍完整 CRUD ====================
if __name__ == "__main__":
    print("=== 1. 新增 (Create) ===")
    new_id = add_goods("测试商品-鼠标", 99.00, 500, "2024-09-01", is_sale=1, cat_id=4)
    print("新商品 good_id =", new_id)

    print("\n=== 2. 按 ID 查询 (Read) ===")
    print(get_goods_by_id(new_id))

    print("\n=== 3. 列表查询（名称含『华为』）===")
    for g in get_goods_list(keyword="华为"):
        print(g)

    print("\n=== 4. 更新价格 (Update) ===")
    print("受影响行数 =", update_goods(new_id, price=79.00))
    print("改完后再查:", get_goods_by_id(new_id))

    print("\n=== 5. 删除 (Delete) ===")
    print("受影响行数 =", delete_goods(new_id))
    print("删除后再查:", get_goods_by_id(new_id))
