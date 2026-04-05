from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from enum import Enum


class UserRole(str, Enum):
    admin = "admin"
    analyst = "analyst"
    viewer = "viewer"

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.viewer 

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: UserRole 
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None
    username: Optional[str] = None
