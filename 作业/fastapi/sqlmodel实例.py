# -*- coding: utf-8 -*-
"""
FastAPI 入口 + 路由层。

这个文件只负责三件事：声明路径和请求体、注入 Session、转发给 CRUD 层。

依赖方向（单向，不能反向）：
    sqlmodel实例.py  →  crud.py  →  models.py
                     →  database.py

上一版把整个项目都塞在这一个文件里，现在东西都拆出去了，
所以这里只需要 import 路由要用的那几个名字 —— 不再需要
create_engine / Session / SQLModel / Column 这些东西了。

启动：python sqlmodel实例.py，然后浏览器打开 http://127.0.0.1:9000/docs
"""
import os

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from crud import (
    create_department,
    create_employee,
    list_departments,
    list_employees,
    read_department,
    read_employee,
    remove_department,
    remove_employee,
    search_employees_by_name,
    update_employee,
)
from database import SessionDep
from models import (
    ApiResponse,
    Department,
    DepartmentCreate,
    Employee,
    EmployeeCreate,
    EmployeePatch,
)

# ==================== Swagger UI 离线 ====================
# /docs 默认从 cdn.jsdelivr.net 拉 Swagger UI 的 JS/CSS，代理或网络不通时页面就是白屏。
# 这里改用同目录下已下载好的 swagger_ui/ 资源，彻底离线。
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SWAGGER_UI_DIR = os.path.join(BASE_DIR, "swagger_ui")
_HAS_LOCAL_UI = os.path.isdir(SWAGGER_UI_DIR)

# 有本地资源就关掉默认的 /docs，再挂自己那个（同名路由谁先注册谁生效）
app = FastAPI(
    title="员工接口",
    description="读写已有旧表 a_my_store.t_employee",
    docs_url=None if _HAS_LOCAL_UI else "/docs",
    redoc_url=None,
)

if _HAS_LOCAL_UI:
    app.mount("/static", StaticFiles(directory=SWAGGER_UI_DIR), name="static")

    @app.get("/docs", include_in_schema=False)
    def custom_swagger_ui():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - 接口文档",
            swagger_js_url="/static/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui.css",
        )
else:
    print("提示：没找到 swagger_ui 目录，/docs 会走 CDN，网络不通时可能白屏")


# ==================== 统一异常处理 ====================
# 成功响应统一成 {code, msg, data} 之后，FastAPI 抛 HTTPException 时默认还是返回
# {"detail": "..."} —— 前端就得写两套解析逻辑，等于没统一。这里把它也转成同一格式。
#
# 注意：422（请求体校验失败）走的是 RequestValidationError，不经过这个 handler，
# 所以字段填错时仍返回 FastAPI 原生的详细结构 —— 那对排查问题更有用，故意不覆盖。
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiResponse(code=exc.status_code, msg=str(exc.detail)).model_dump(),
    )


# ==================== 路由层 ====================
# response_model=ApiResponse[Xxx] 里的泛型参数会写进 OpenAPI 文档，
# 所以 Swagger 上 data 的结构跟以前完全一样，没丢类型信息。
@app.post("/employees", response_model=ApiResponse[Employee], summary="新增员工")
def api_create_employee(data: EmployeeCreate, session: SessionDep):
    """
    请求体传完整员工信息，id 不要传（交给数据库自增）。
    薪资上限 99999999.99（跟数据库 DECIMAL(10,2) 对齐），超了直接 422。
    职位编号/部门编号/领导编号必须在对应表里真实存在，否则外键报错。
    """
    return ApiResponse(data=create_employee(session, data))


@app.get("/employees", response_model=ApiResponse[list[Employee]], summary="查询全部员工")
def api_list_employees(session: SessionDep):
    return ApiResponse(data=list_employees(session))



# 按名字查必须换个路径：/employees/{name} 跟 /employees/{employee_id}
# 是同一个路径形状，FastAPI 按注册顺序匹配，先注册的永远命中，
# 而且 /employees/张三 会卡在 int 转换上直接 422。
@app.get(
    "/employees/by-name/{name}",
    response_model=ApiResponse[list[Employee]],
    summary="按姓名查询",
)
def api_search_employees(name: str, session: SessionDep):
    return ApiResponse(data=search_employees_by_name(session, name))


@app.get("/employees/{employee_id}", response_model=ApiResponse[Employee], summary="按编号查询")
def api_read_employee(employee_id: int, session: SessionDep):
    return ApiResponse(data=read_employee(session, employee_id))


@app.patch("/employees/{employee_id}", response_model=ApiResponse[Employee], summary="局部更新")
def api_update_employee(employee_id: int, patch: EmployeePatch, session: SessionDep):
    """
    请求体只写要改的字段，例如：
        {"name": "李四", "salary": "13000.00"}
    想清空可空字段（奖金比例 / 职位编号 / 领导编号 / 部门编号）就传 null：
        {"bonus_pct": null}

    小提示：薪资、奖金比例是 DECIMAL，JSON 里用字符串 "13000.00" 传比用数字
    13000.0 更保险，能避开浮点精度问题。
    """
    return ApiResponse(data=update_employee(session, employee_id, patch))


@app.delete("/employees/{employee_id}", response_model=ApiResponse[dict], summary="删除员工")
def api_remove_employee(employee_id: int, session: SessionDep):
    return ApiResponse(data=remove_employee(session, employee_id))


# ==================== 部门路由（前端页面用的单数路径 /department） ====================
# myproject/static 里的页面写死的是 /department 和 /employee（单数），
# 这里按页面的路径补齐；库里 t_department 列名是中文，映射见 models.Department。

@app.get("/department", response_model=ApiResponse[list[Department]], summary="查询全部部门")
def api_list_departments(session: SessionDep):
    return ApiResponse(data=list_departments(session))


@app.post("/department", response_model=ApiResponse[Department], summary="新增部门")
def api_create_department(data: DepartmentCreate, session: SessionDep):
    """请求体 {"name": "研发部", "description": "负责研发工作"}，两项都必填"""
    return ApiResponse(code=201, msg="创建成功", data=create_department(session, data))


@app.get(
    "/department/{department_id}",
    response_model=ApiResponse[Department],
    summary="按编号查询部门",
)
def api_read_department(department_id: int, session: SessionDep):
    return ApiResponse(data=read_department(session, department_id))


@app.delete(
    "/department/{department_id}",
    response_model=ApiResponse[dict],
    summary="删除部门",
)
def api_remove_department(department_id: int, session: SessionDep):
    """部门下还有员工时外键会拦住，返回 400 和一句人话提示"""
    return ApiResponse(data=remove_department(session, department_id))


# ==================== 员工单数别名（页面写死的是 /employee） ====================
# 复用上面 /employees 的同一套 crud 函数，只是多开几个路径给页面用。

@app.get("/employee", response_model=ApiResponse[list[Employee]], summary="查询全部员工（页面用）")
def api_list_employees_alias(session: SessionDep):
    return ApiResponse(data=list_employees(session))


@app.post("/employee", response_model=ApiResponse[Employee], summary="新增员工（页面用）")
def api_create_employee_alias(data: EmployeeCreate, session: SessionDep):
    return ApiResponse(code=201, msg="创建成功", data=create_employee(session, data))


@app.delete(
    "/employee/{employee_id}",
    response_model=ApiResponse[dict],
    summary="删除员工（页面用）",
)
def api_remove_employee_alias(employee_id: int, session: SessionDep):
    return ApiResponse(data=remove_employee(session, employee_id))

# ==================== 主程序 ====================
# 静态目录必须用「相对这个文件本身」的绝对路径：
# 原来写的是相对路径 "作业/fastapi/.../static"，只有在 py.py 目录下启动才成立，
# 换个工作目录（比如直接在作业/fastapi 下跑）就报 Directory does not exist。
# ⚠️ mount("/") 必须写在所有 @app 路由之后：Starlette 按注册顺序匹配，
#    挂载在前会把后面注册的 API 路由全部吞掉（请求全落到静态文件 404）。
# 另外加一层判断：目录真没有时只警告不崩，服务照样能起、接口照样能用。
STATIC_DIR = os.path.join(BASE_DIR, "5_FastAPI与SQLAlchemy结合", "myproject", "static")
if os.path.isdir(STATIC_DIR):
    app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
else:
    print(f"[警告] 静态目录不存在，跳过挂载：{STATIC_DIR}")

if __name__ == "__main__":
    # 直接传 app 对象最省事（文件名是中文，用导入字符串容易出问题）。
    # 想开 reload=True 的话 uvicorn 要求传「导入字符串」，
    # 那就先把这个文件改名成英文（比如 main.py），再写 uvicorn.run("main:app", reload=True)。
    uvicorn.run(app, host="127.0.0.1", port=9000)