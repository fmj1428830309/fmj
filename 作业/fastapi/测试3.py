from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlmodel import select
from typing import List

from database import init_db, get_db
from models import (
    Department, DepartmentCreate, DepartmentRead,
    Employee, EmployeeCreate, EmployeeRead
)


# ========== lifespan 启动事件 ==========
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="FastAPI + SQLModel 部门员工管理", lifespan=lifespan)


# ==================== 根路径 ====================
@app.get("/")
def root():
    return {"message": "部门员工管理系统", "docs": "/docs"}


# ==================== Department（部门）====================

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


@app.get("/departments/", response_model=List[DepartmentRead])
def read_departments(db: Session = Depends(get_db)):
    return db.exec(select(Department)).all()


@app.get("/departments/{dept_id}", response_model=DepartmentRead)
def read_department(dept_id: int, db: Session = Depends(get_db)):
    dept = db.get(Department, dept_id)
    if not dept:
        raise HTTPException(status_code=404, detail="部门不存在")
    return dept


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


@app.delete("/departments/{dept_id}")
def delete_department(dept_id: int, db: Session = Depends(get_db)):
    dept = db.get(Department, dept_id)
    if not dept:
        raise HTTPException(status_code=404, detail="部门不存在")
    db.delete(dept)
    db.commit()
    return {"message": "部门删除成功"}


# ==================== Employee（员工）====================

@app.post("/employees/", response_model=EmployeeRead)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    # 如果指定了部门，先检查部门是否存在
    if emp.department_id is not None:
        dept = db.get(Department, emp.department_id)
        if not dept:
            raise HTTPException(status_code=404, detail="所属部门不存在")

    db_emp = Employee(**emp.model_dump())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp


@app.get("/employees/", response_model=List[EmployeeRead])
def read_employees(db: Session = Depends(get_db)):
    return db.exec(select(Employee)).all()


@app.get("/employees/{emp_id}", response_model=EmployeeRead)
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.get(Employee, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="员工不存在")
    return emp


@app.put("/employees/{emp_id}", response_model=EmployeeRead)
def update_employee(emp_id: int, emp: EmployeeCreate, db: Session = Depends(get_db)):
    db_emp = db.get(Employee, emp_id)
    if not db_emp:
        raise HTTPException(status_code=404, detail="员工不存在")

    # 如果修改了部门，检查新部门是否存在
    if emp.department_id is not None and emp.department_id != db_emp.department_id:
        dept = db.get(Department, emp.department_id)
        if not dept:
            raise HTTPException(status_code=404, detail="所属部门不存在")

    db_emp.name = emp.name
    db_emp.age = emp.age
    db_emp.hire_date = emp.hire_date
    db_emp.department_id = emp.department_id
    db.commit()
    db.refresh(db_emp)
    return db_emp


@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.get(Employee, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="员工不存在")
    db.delete(emp)
    db.commit()
    return {"message": "员工删除成功"}


# ==================== 关联查询：某部门下的员工 ====================
@app.get("/departments/{dept_id}/employees", response_model=List[EmployeeRead])
def read_department_employees(dept_id: int, db: Session = Depends(get_db)):
    dept = db.get(Department, dept_id)
    if not dept:
        raise HTTPException(status_code=404, detail="部门不存在")
    return db.exec(select(Employee).where(Employee.department_id == dept_id)).all()


# ==================== 启动 ====================
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("测试3:app", host="0.0.0.0", port=8082, reload=True)
