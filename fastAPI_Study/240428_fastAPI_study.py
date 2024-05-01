from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# 메인페이지
@app.get("/")
async def main(request: Request):
    client_ip = request.client.host
    print(f"======= 방문자의 IP 주소: {client_ip}")
    return FileResponse('index.html')

# 데이터
@app.get("/data")
async def data():
    return {'hello' : 12345}


class Model(BaseModel):
    name :str
    phone :int


# 데이터 받아오기
@app.post("/send")
async def send(data : Model):
    print(data)
    return '전송완료'