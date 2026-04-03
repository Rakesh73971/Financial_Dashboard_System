from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.financial_record import Transaction, TransactionType
from sqlalchemy import func


def get_summary(db: Session, user_id: int):
    income = db.query(func.sum(Transaction.amount)).filter(
        Transaction.user_id == user_id,
        Transaction.type == TransactionType.income,
        Transaction.is_deleted == False
    ).scalar() or 0

    expense = db.query(func.sum(Transaction.amount)).filter(
        Transaction.user_id == user_id,
        Transaction.type == TransactionType.expense,
        Transaction.is_deleted == False
    ).scalar() or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }

def get_category_summary(db: Session, user_id: int):
    results = db.query(
        Transaction.category,
        func.sum(Transaction.amount)
    ).filter(
        Transaction.user_id == user_id,
        Transaction.is_deleted == False
    ).group_by(Transaction.category).all()

    return [{"category": r[0], "total": r[1]} for r in results]


def get_monthly_summary(db: Session, user_id: int):
    results = db.query(
        func.to_char(Transaction.date, 'YYYY-MM'),
        func.sum(Transaction.amount)
    ).filter(
        Transaction.user_id == user_id,
        Transaction.is_deleted == False
    ).group_by(func.to_char(Transaction.date, 'YYYY-MM')).all()

    return [{"month": r[0], "total": r[1]} for r in results]

def get_recent_transactions(db: Session, user_id: int):
    return db.query(Transaction).filter(
        Transaction.user_id == user_id,
        Transaction.is_deleted == False
    ).order_by(Transaction.date.desc()).limit(5).all()