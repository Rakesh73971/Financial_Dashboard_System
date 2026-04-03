from pydantic import BaseModel, EmailStr, ConfigDict

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

    # Use the V2 ConfigDict approach here:
    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: str
    password: str