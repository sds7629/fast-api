from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn
from typing import Optional

user_router = APIRouter(tags=["User"])

users = {
    "sds7629@naver.com": User(email="sds7629@naver.com", password="1234", events=[])
}


@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists",
        )
    users[data.email] = data
    return {
        "message": "User successfully registered",
    }


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exists",
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed",
        )
    return {
        "message": "User Signed in successfully",
    }
