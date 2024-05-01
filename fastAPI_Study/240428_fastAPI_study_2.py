from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()
router = APIRouter()

@app.get("/")
async def welcome() -> dict:
    return {
        "message" : "Hello World"
    }


@router.get("/hello")
async def say_hello() -> dict:
    return {
        "message" : "Hello!"
    }