from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from sqlmodel import SQLModel, select

from crud import CreateUser, UpdateUser, list_User, read_User, remove_User
from database import SessionDep, engine
from models import ApiResponse, User, UserCreate, UserPatch


@asynccontextmanager
async def lifespan_manager(app: FastAPI):
    # t_user 是已存在的老表，create_all 会先检查、存在就跳过，所以是安全的。
    SQLModel.metadata.create_all(engine)
    print("FastApi 启动之前 - 初始化操作：建表、加载全局配置")
    yield
    print("FastApi 启动之后 - 释放资源操作：关闭数据库连接")
    engine.dispose()


app = FastAPI(lifespan=lifespan_manager)

# index.html 可能被浏览器以 file:// 直接打开（这时 origin 是 null），
# 放开 CORS 才能正常跨域调接口；通过 127.0.0.1:8000 访问时本来就同源，不影响。
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """让业务错误也走统一格式 {code, msg, data}，不然成功和失败两套格式。"""
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiResponse(code=exc.status_code, msg=str(exc.detail)).model_dump(),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """参数校验失败（422）也统一格式，顺便把出错字段提示给前端。"""
    errors = exc.errors()
    first = errors[0] if errors else {}
    loc = ".".join(str(i) for i in first.get("loc", ()))
    msg = f"参数错误：{loc} {first.get('msg', '')}" if loc else "参数错误"
    return JSONResponse(
        status_code=422,
        content=ApiResponse(code=422, msg=msg, data=errors).model_dump(),
    )


BASE_DIR = Path(__file__).resolve().parent


@app.get("/", include_in_schema=False, summary="前端页面")
def index():
    """访问 http://127.0.0.1:8000/ 直接打开 CRUD 页面，省得手动找文件。"""
    page = BASE_DIR / "index.html"
    if not page.is_file():
        return JSONResponse({"code": 404, "msg": "index.html 不存在", "data": None})
    return FileResponse(page)


# ---------------------------------------------------------------- 查询
@app.get("/user", response_model=ApiResponse[list[User]], summary="查询所有人")
def api_list_user(session: SessionDep):
    return ApiResponse(data=list_User(session))


# 【注意顺序】/user/by-name/{name} 必须写在 /user/{user_id} 前面：
# FastAPI 按注册顺序匹配，反过来的话 "by-name" 会被当成 user_id 去转 int，直接 422。
@app.get(
    "/user/by-name/{name}",
    response_model=ApiResponse[list[User]],
    summary="按名称模糊查询",
)
def api_list_user_by_name(name: str, session: SessionDep):
    users = session.exec(select(User).where(User.name.contains(name))).all()
    return ApiResponse(data=users)


@app.get("/user/{user_id}", response_model=ApiResponse[User], summary="按编号查询")
def api_read_user(user_id: int, session: SessionDep):
    return ApiResponse(data=read_User(session, user_id))


# ---------------------------------------------------------------- 新增
@app.post("/user", response_model=ApiResponse[User], summary="新增用户")
def api_create_user(data: UserCreate, session: SessionDep):
    return ApiResponse(code=201, msg="创建成功", data=CreateUser(session, data))


# ---------------------------------------------------------------- 修改
@app.patch("/user/{user_id}", response_model=ApiResponse[User], summary="局部更新用户")
def api_patch_user(user_id: int, patch: UserPatch, session: SessionDep):
    return ApiResponse(data=UpdateUser(session, user_id, patch))


# ---------------------------------------------------------------- 删除
@app.delete("/user/{user_id}", response_model=ApiResponse[dict], summary="删除用户")
def api_delete_user(user_id: int, session: SessionDep):
    user = remove_User(session, user_id)
    return ApiResponse(data={"id": user.id, "name": user.name})


if __name__ == "__main__":
    uvicorn.run(
        app="接口:app",
        host="127.0.0.1",
        port=8001,
        reload=True,
    )
