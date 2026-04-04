from app.models.financial_record import Transaction

def create_transaction(db, user_id, data):
    transaction = Transaction(
        user_id=user_id,
        amount=data.amount,
        type=data.type,
        category=data.category,
        date=data.date,
        notes=data.notes
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


def get_transactions(db, user_id, filters, skip=0, limit=10):
    query = db.query(Transaction).filter(
        Transaction.user_id == user_id,
        Transaction.is_deleted == False
    )

    if filters.get("type"):
        query = query.filter(Transaction.type == filters["type"])

    if filters.get("category"):
        query = query.filter(Transaction.category == filters["category"])

    if filters.get("start_date"):
        query = query.filter(Transaction.date >= filters["start_date"])

    if filters.get("end_date"):
        query = query.filter(Transaction.date <= filters["end_date"])

    
    total = query.count()

    data = query.order_by(Transaction.date.desc()).offset(skip).limit(limit).all()

    return {
        "total": total,
        "data": data
    }


def update_transaction(db, transaction_id, user_id, data):
    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.user_id == user_id,
        Transaction.is_deleted == False
    ).first()

    if not transaction:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(transaction, key, value)

    db.commit()
    db.refresh(transaction)
    return transaction


def delete_transaction(db, transaction_id, user_id):
    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.user_id == user_id
    ).first()

    if not transaction:
        return None

    transaction.is_deleted = True
    db.commit()
    return transaction