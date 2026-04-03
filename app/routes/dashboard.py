from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.dashboard_service import *
from app.core.permissions import require_role

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/summary")
def summary(
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["analyst", "admin"]))
):
    return get_summary(db, current_user.id)

@router.get("/category")
def category_summary(
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["analyst", "admin"]))
):
    return get_category_summary(db, current_user.id)



@router.get("/monthly")
def monthly_summary(
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["analyst", "admin"]))
):
    return get_monthly_summary(db, current_user.id)

@router.get("/recent")
def recent(
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["analyst", "admin"]))
):
    return get_recent_transactions(db, current_user.id)