# 3.2 第一个 FastAPI 程序
# 依赖安装：pip install fastapi  /  pip install uvicorn
# 启动：uvicorn main:app --reload   （或直接运行本文件）

from fastapi import FastAPI
import uvicorn

app = FastAPI()


# 同步函数（没有 async）：
# 本质：普通同步函数，内部不能使用 await，会阻塞当前线程直到完成。
# 适用：纯计算逻辑、或只支持同步的库。
# 执行机制：FastAPI 自动放入线程池（默认 os.cpu_count() * 5）执行，
# 多请求会分配到不同线程并行，但单线程内仍会阻塞。
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# 异步函数（async def）：
# 本质：异步协程，内部可用 await 调用其他异步操作。
# 适用：I/O 密集型操作（网络、文件、数据库）且有对应异步库。
# 执行机制：FastAPI 用 asyncio 处理，遇到 await 让出控制权给事件循环，
# 在等待 I/O 期间继续处理其他请求，真正的异步并发。


@app.get("/async")
async def read_root_async():
    return {"Hello": "World"}


if __name__ == "__main__":
    # 直接在代码中启动 uvicorn 服务器
    uvicorn.run(
        app="main:app",       # 指定要运行的 FastAPI 应用实例
        host="0.0.0.0",       # 允许外部访问（本地可通过 127.0.0.1 或 localhost）
        port=8000,            # 端口号
        reload=True           # 开发模式：代码修改后自动重启（生产环境需去掉）
    )
