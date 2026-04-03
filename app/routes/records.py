from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.transaction import *
from app.services.record_service import *
from app.core.permissions import require_role


router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=TransactionResponse)
def create(
    data: TransactionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["admin"]))
):
    return create_transaction(db, current_user.id, data)


@router.get("/")
def get_all_transactions(
    type: str = Query(None),
    category: str = Query(None),
    start_date: str = Query(None),
    end_date: str = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["analyst", "admin"]))
):
    filters = {
        "type": type,
        "category": category,
        "start_date": start_date,
        "end_date": end_date
    }

    return get_transactions(db, current_user.id, filters, skip, limit)


@router.put("/{transaction_id}", response_model=TransactionResponse)
def update(
    transaction_id: int,
    data: TransactionUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["admin"]))
):
    transaction = update_transaction(db, transaction_id, current_user.id, data)

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return transaction


@router.delete("/{transaction_id}")
def delete(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["admin"]))
):
    transaction = delete_transaction(db, transaction_id, current_user.id)

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return {"message": "Transaction deleted"}