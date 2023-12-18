from fastapi import FastAPI
from models.users import User, Gender, Role
from uuid import UUID, uuid4
from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/home/{name}")
async def read_name(name: str):
    return {"name": name}
