from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.user import UserResponse, UserUpdate
from app.core.permissions import require_role
from app.services.user_service import get_all_users, update_user 

router = APIRouter(prefix="/users", tags=["User Management"])

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[UserResponse])
def read_all_users(
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["admin"]))
):
    return get_all_users(db)

@router.get("/me", status_code=status.HTTP_200_OK, response_model=UserResponse)
def get_my_profile(
    current_user=Depends(require_role(["viewer", "analyst", "admin"]))
):
    
    return current_user

@router.patch("/{user_id}", status_code=status.HTTP_202_ACCEPTED, response_model=UserResponse)
def update_user_access(
    user_id: int,
    updates: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["admin"]))
):
   
    updated_user = update_user(db, user_id=user_id, updates=updates)
    
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )
    
    return updated_user