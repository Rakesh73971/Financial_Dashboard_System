from fastapi import APIRouter, Depends,status,Request
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.dashboard_service import *
from app.core.permissions import require_role
from app.core.rate_limiter import limiter

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary", status_code=status.HTTP_200_OK)
@limiter.limit("60/minute")
def summary(
    requrest: Request,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["viewer", "analyst", "admin"])) 
):
    return get_summary(db, current_user.id)


@router.get("/category", status_code=status.HTTP_200_OK)
@limiter.limit("60/minute")
def category_summary(
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["viewer", "analyst", "admin"]))
):
    return get_category_summary(db, current_user.id)



@router.get("/monthly", status_code=status.HTTP_200_OK)
@limiter.limit("60/minute")
def monthly_summary(
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["viewer", "analyst", "admin"]))
):
    return get_monthly_summary(db, current_user.id)


@router.get("/recent", status_code=status.HTTP_200_OK)
@limiter.limit("60/minute")
def recent(
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["viewer", "analyst", "admin"]))
):
    return get_recent_transactions(db, current_user.id)