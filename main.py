from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
from db.connection import conn

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
def start_event():
    conn()
