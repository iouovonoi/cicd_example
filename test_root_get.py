'''
Author: ChiaEnKang
Date: 2022-12-06 08:07:27
LastEditors: ChiaEnKang
LastEditTime: 2022-12-06 08:24:09
'''
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}