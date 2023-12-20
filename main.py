from fastapi import FastAPI
from routes.users import user_router

import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/user")
