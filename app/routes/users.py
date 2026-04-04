from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.user import UserResponse, UserUpdate
from app.models.user import User
from app.core.permissions import require_role

router = APIRouter(prefix="/users", tags=["User Management"])

@router.get("/", response_model=List[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["admin"]))
):

    return db.query(User).all()

@router.get("/me", response_model=UserResponse)
def get_my_profile(
    current_user=Depends(require_role(["viewer", "analyst", "admin"]))
):

    return current_user

@router.patch("/{user_id}", response_model=UserResponse)
def update_user_status_or_role(
    user_id: int,
    updates: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["admin"]))
):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    

    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user