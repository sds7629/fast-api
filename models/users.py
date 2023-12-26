from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event
from sqlalchemy import Column, Integer, TEXT, VARCHAR, ForeignKey
from db.connection import Base

# class EmptyStringValidator(Validator):
#     """
#     Validate whether a string is empty.
#     """
#     def __call__(self, value: str):
#         if not value:
#             raise ValidationError(f"Value can not be empty")


class User(Base):
    __tablename__ = "USER"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(VARCHAR(100), nullable=False)
    password = Column(VARCHAR(20), nullable=False)
    events = Column(Integer, ForeignKey("EVENT"))


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong",
                "events": [],
            }
        }


### Tortoise ORM

# from tortoise import fields, models
# from tortoise.contrib.pydantic import pydantic_model_creator


# class Users(models.Model):
#     """
#     The User model
#     """

#     id = fields.IntField(pk=True)
#     #: This is a username
#     username = fields.CharField(max_length=20, unique=True)
#     name = fields.CharField(max_length=50, null=True)
#     family_name = fields.CharField(max_length=50, null=True)
#     category = fields.CharField(max_length=30, default="misc")
#     password_hash = fields.CharField(max_length=128, null=True)
#     created_at = fields.DatetimeField(auto_now_add=True)
#     modified_at = fields.DatetimeField(auto_now=True)

#     def full_name(self) -> str:
#         """
#         Returns the best name
#         """
#         if self.name or self.family_name:
#             return f"{self.name or ''} {self.family_name or ''}".strip()
#         return self.username

#     class PydanticMeta:
#         computed = ["full_name"]
#         exclude = ["password_hash"]


# User_Pydantic = pydantic_model_creator(Users, name="User")
# UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
