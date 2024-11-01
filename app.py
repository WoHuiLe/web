from fastapi import FastAPI, Request, Response, Depends
from fastapi.middleware.cors import CORSMiddleware  # 导入 CORS 中间件
from pydantic import BaseModel  # 用于请求体的数据验证
from starlette.responses import FileResponse
from typing import Optional
import os
import sys
import asyncio

this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_dir)
import uvicorn

import base64
import subprocess
import traceback
import math
import numpy as np
import time
import datetime
import json
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, WebSocket

from routes.get_data import GetDataRouter
from start_flask import app
import uvicorn


class FastIO:
    def __init__(self) -> None:
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
        )
        self.include_router()
        uvicorn.run(self.app, host="0.0.0.0", port=6111, access_log=False)

    def include_router(self):
        get_data_router = GetDataRouter()
        self.app.include_router(get_data_router, tags="get_data")


if __name__ == "__main__":
    import threading
    # FastIO()
    threading.Thread(target=FastIO).start()
    threading.Thread(target=app.run, args=("0.0.0.0", 1111)).start()
   
    
    # app.run(host="0.0.0.0", port=1111, debug=True)
   
