"""
前端页面启动脚本（学习辅助，独立文件，不修改 测试2.py / models.py / database.py）

作用：
1. 用 http.server 提供一个静态网页 index.html
2. 把前端发来的 /api/* 请求转发到 8080 端口的「测试2.py」FastAPI 服务，
   从而绕开浏览器跨域（CORS）限制 —— 因为 测试2.py 没有开 CORS。

用法（两个终端窗口）：
  终端 A：先启动后端
      python 测试2.py          # 会监听 8080
  终端 B：再启动本前端
      python serve_frontend.py  # 会监听 8081

然后浏览器打开：http://127.0.0.1:8081
"""

import http.server
import urllib.request
import urllib.error
import os

BACKEND_HOST = "127.0.0.1"
BACKEND_PORT = 8080          # 测试2.py 的端口
FRONTEND_PORT = 8081         # 前端页面的端口
STATIC_DIR = os.path.dirname(os.path.abspath(__file__))  # 当前目录


class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # 让静态文件从脚本所在目录读取
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    # 转发 /api/* 到后端
    def _proxy(self):
        # 原始路径形如 /api/departments/，去掉 /api 前缀
        target_path = self.path.replace("/api", "", 1)
        backend_url = f"http://{BACKEND_HOST}:{BACKEND_PORT}{target_path}"

        # 读取请求体（POST/PUT 的 JSON）
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length else None

        req = urllib.request.Request(backend_url, data=body, method=self.command)
        # 透传关键请求头
        if body:
            req.add_header("Content-Type", self.headers.get("Content-Type", "application/json"))

        try:
            with urllib.request.urlopen(req) as resp:
                data = resp.read()
                self.send_response(resp.status)
                self.send_header("Content-Type", resp.headers.get("Content-Type", "application/json"))
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
        except urllib.error.HTTPError as e:
            # 后端返回 4xx/5xx（如 404），也要原样回传给前端
            data = e.read()
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except urllib.error.URLError as e:
            # 后端没启动
            msg = '{"detail": "无法连接后端，请先运行 python 测试2.py"}'.encode("utf-8")
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(msg)))
            self.end_headers()
            self.wfile.write(msg)

    def do_GET(self):
        if self.path.startswith("/api"):
            self._proxy()
        else:
            super().do_GET()

    def do_POST(self):
        if self.path.startswith("/api"):
            self._proxy()
        else:
            super().do_POST()

    def do_PUT(self):
        if self.path.startswith("/api"):
            self._proxy()
        else:
            super().do_PUT()

    def do_DELETE(self):
        if self.path.startswith("/api"):
            self._proxy()
        else:
            super().do_DELETE()


if __name__ == "__main__":
    print(f"前端页面已启动：http://127.0.0.1:{FRONTEND_PORT}")
    print(f"后端代理目标：  http://{BACKEND_HOST}:{BACKEND_PORT}  （请先运行 `python 测试2.py`）")
    server = http.server.ThreadingHTTPServer(("127.0.0.1", FRONTEND_PORT), ProxyHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")
