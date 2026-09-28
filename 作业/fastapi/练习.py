from typing import Optional
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel, Field, create_engine, Session, select

app = FastAPI()
class Dept(SQLModel, table=True):
    __tablename__ = "dept"
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    gender: Optional[str] = None
engine = create_engine(
    "mysql+pymysql://root:203227944fmj@127.0.0.1:3306/mytest01",
    echo=True
)

@app.post("/dept")
def add_dept(dept: Dept):
    with Session(engine) as session:
        session.add(dept)
        session.commit()
        session.refresh(dept)
        return dept


@app.get("/dept/search/{dept_name}")
def get_dept_by_name(dept_name: str):
    with Session(engine) as session:
        statement = select(Dept).where(Dept.name == dept_name)
        dept = session.exec(statement).first()
        if dept is None:
            return {"message": "部门不存在"}
        return dept

@app.get("/dept/{dept_id}")
def get_dept(dept_id: int):
    with Session(engine) as session:

        dept = session.get(Dept, dept_id)
        if dept is None:
            return {"message": "部门不存在"}

        return dept

@app.delete("/dept/{dept_id}")
def delect_dept_by_id(dept_id: int):
    with Session(engine) as session:

        dept = session.get(Dept, dept_id)
        if dept is None:
            return {"message": "部门不存在"}
        session.delete(dept)
        session.commit()
        return {"message": "部门删除成功"}

@app.get("/dept")
def get_all_depts():
    with Session(engine) as session:
        statement = select(Dept)
        depts = session.exec(statement).all()
        print(depts)
        return depts
# ---------- 静态页面挂载 ----------
# 把 HTML 文件放在同级 static 目录下，FastAPI 直接提供
from pathlib import Path
STATIC_DIR = Path(__file__).parent / "static"
STATIC_DIR.mkdir(exist_ok=True)
app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")
if  __name__ == "__main__":
    import uvicorn
    uvicorn.run("练习:app", host="0.0.0.0", port=8084, reload=True)



    # 更新测试
    # update_dept(5, "销售部", "男")
    # print("更新后：", get_dept(5))
    # get_all_depts()
     # add_dept(Dept(name="销售部", gender="男"))
    # add_dept(Dept(name="销售部", gender="男"))
    # add_dept(Dept(name="采购部", gender="男"))
    # add_dept(Dept(name="销售部", gender="女"))
    # add_dept(Dept(name="采购部", gender="男"))
    # print(get_all_depts())
    # 插入测试数据
    # add_dept(Dept(name="销售部", gender="男"))
    # add_dept(Dept(name="采购部", gender="男"))
    # add_dept(Dept(name="研发部", gender="女"))

    # 查询测试
    # print("ID=100：", get_dept(100))
    # print("名字=销售部：", get_dept_by_name("销售部"))


    # print("名字=销售部：", get_dept_by_name("销售部"))
    # print("删除 ID=1：", delect_dept_by_id(1))
    # print("删除后全部：", get_all_depts())
