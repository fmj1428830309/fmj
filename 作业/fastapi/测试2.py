from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlmodel import select
from typing import List

from database import init_db, get_db
from models import Department, DepartmentCreate, DepartmentRead


# ========== 新版 lifespan 事件 ==========
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行：建表
    init_db()
    yield
    # 关闭时执行（可选）


app = FastAPI(title="FastAPI + SQLModel 部门管理", lifespan=lifespan)


# ==================== 新增部门 ====================
@app.post("/departments/", response_model=DepartmentRead)
def create_department(dept: DepartmentCreate, db: Session = Depends(get_db)):
    existing = db.exec(select(Department).where(Department.name == dept.name)).first()
    if existing:
        raise HTTPException(status_code=400, detail="部门名称已存在")
    db_dept = Department(name=dept.name, location=dept.location)
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept


# ==================== 查询全部 ====================
@app.get("/departments/", response_model=List[DepartmentRead])
def read_departments(db: Session = Depends(get_db)):
    statement = select(Department)
    depts = db.exec(statement).all()
    return depts
@app.put("/departments/{dept_id}",response_model=DepartmentRead)
def update_department(dept_id: int, dept: DepartmentCreate, db: Session = Depends(get_db)):
    db_dept = db.get(Department, dept_id)
    if not db_dept:
        raise HTTPException(status_code=404, detail="部门不存在")
    if dept.name != db_dept.name:
        existing = db.exec(select(Department).where(Department.name == dept.name)).first()
        if existing:
            raise HTTPException(status_code=400, detail="部门名称已存在")
    db_dept.name = dept.name
    db_dept.location = dept.location
    db.commit()
    db.refresh(db_dept)
    return db_dept

# ==================== 根据 ID 查询 ====================
@app.get("/departments/{dept_id}", response_model=DepartmentRead)
def read_department(dept_id: int, db: Session = Depends(get_db)):
    dept = db.get(Department, dept_id)
    if not dept:
        raise HTTPException(status_code=404, detail="部门不存在")
    return dept


# ==================== 修改部门 ====================
@app.put("/departments/{dept_id}", response_model=DepartmentRead)
def update_department(dept_id: int, dept: DepartmentCreate, db: Session = Depends(get_db)):
    db_dept = db.get(Department, dept_id)
    if not db_dept:
        raise HTTPException(status_code=404, detail="部门不存在")

    if dept.name != db_dept.name:
        existing = db.exec(select(Department).where(Department.name == dept.name)).first()
        if existing:
            raise HTTPException(status_code=400, detail="部门名称已存在")

    db_dept.name = dept.name
    db_dept.location = dept.location
    db.commit()
    db.refresh(db_dept)
    return db_dept


# ==================== 删除部门 ====================
@app.delete("/departments/{dept_id}")
def delete_department(dept_id: int, db: Session = Depends(get_db)):
    dept = db.get(Department, dept_id)
    if not dept:
        raise HTTPException(status_code=404, detail="部门不存在")

    db.delete(dept)
    db.commit()
    return {"message": "部门删除成功"}
@app.get("/")
def root():
    return {"message": "FastAPI + SQLModel 部门管理系统", "docs": "/docs"}


# ==================== 启动 ====================
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("测试2:app", host="0.0.0.0", port=8080, reload=True)
