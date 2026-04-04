from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from fastapi.security import OAuth2PasswordRequestForm
from app.services.user_service import create_user, authenticate_user
from app.db.session import get_db
from app.schemas.user import UserResponse
from app.core.security import create_access_token


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register",status_code=status.HTTP_201_CREATED,response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.post("/login",status_code=status.HTTP_202_ACCEPTED)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, email=user_credentials.username, password=user_credentials.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"user_id": user.id}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }