import strawberry
from typing import Optional
from enum import Enum

@strawberry.enum
class Role(Enum):
    USER = "user"
    ADMIN = "admin"

@strawberry.type
class User:
    id: str
    email: str
    name: str
    role: Role
    vk_id: Optional[str] = None
    disabled: bool = False

@strawberry.type
class Token:
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

@strawberry.input
class UserInput:
    email: str
    name: str
    password: str

@strawberry.input
class LoginInput:
    email: str
    password: str 