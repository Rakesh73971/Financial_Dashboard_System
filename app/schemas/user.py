from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)




class UserUpdate(BaseModel):
    role: Optional[str] = None
    is_active: Optional[bool] = None
    username: Optional[str] = None