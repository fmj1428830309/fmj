# 第5章 FastAPI 与 SQLAlchemy 结合案例（扩展）
# 项目结构：
# myproject/
# ├── fastapi_sqlalchemy.py   # FastAPI 主应用（接口定义）
# ├── 接口.py                 # 模型类基类
# ├── database.py             # 数据库配置（引擎、会话）
# └── table_2_models.py       # SQLAlchemy 模型（映射 MySQL 表）

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from table_2_models import Departments, Employees
from database import SessionLocal, engine

app = FastAPI(title="部门管理系统")

# CORS 中间件：允许前端页面（包括 file:// 直接打开）跨域访问接口
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态目录（前端页面所在）
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return RedirectResponse(url="/static/index.html")


# 依赖项：获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 部门相关接口
@app.post("/departments/")
def create_department(name: str, location: str, db: Session = Depends(get_db)):
    db_department = Departments(name=name, location=location)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department


@app.get("/departments/")
def read_departments(db: Session = Depends(get_db)):
    return db.query(Departments).all()


@app.get("/departments/{department_id}")
def read_department(department_id: int, db: Session = Depends(get_db)):
    department = db.query(Departments).filter(Departments.id == department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department


# 修改部门
@app.put("/departments/{department_id}")
def update_department(department_id: int, name: str, location: str, db: Session = Depends(get_db)):
    department = db.query(Departments).filter(Departments.id == department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    department.name = name
    department.location = location
    db.commit()
    db.refresh(department)
    return department


# 删除部门
@app.delete("/departments/{department_id}")
def delete_department(department_id: int, db: Session = Depends(get_db)):
    department = db.query(Departments).filter(Departments.id == department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    db.delete(department)
    db.commit()
    return {"message": f"部门 {department_id} 已删除"}


if __name__ == "__main__":
    uvicorn.run(
        app="fastapi_sqlalchemy:app",  # 指定要运行的 FastAPI 应用实例
        host="0.0.0.0",
        port=8000,
        reload=True
    )
