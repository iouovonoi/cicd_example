'''
Author: ChiaEnKang
Date: 2022-12-06 08:01:47
LastEditors: ChiaEnKang
LastEditTime: 2022-12-06 08:25:17
'''
from fastapi.testclient import TestClient
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello World"}
