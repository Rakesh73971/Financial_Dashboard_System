from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.dashboard_service import *
from app.core.permissions import require_role

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/summary",status_code=status.HTTP_200_OK)
def summary(
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["analyst", "admin"]))
):
    return get_summary(db, current_user.id)

@router.get("/category",status_code=status.HTTP_200_OK)
def category_summary(
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["analyst", "admin"]))
):
    return get_category_summary(db, current_user.id)



@router.get("/monthly",status_code=status.HTTP_200_OK)
def monthly_summary(
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["analyst", "admin"]))
):
    return get_monthly_summary(db, current_user.id)

@router.get("/recent",status_code=status.HTTP_200_OK)
def recent(
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["analyst", "admin"]))
):
    return get_recent_transactions(db, current_user.id)