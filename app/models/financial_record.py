from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey,
    Enum, Numeric, Date, Text, Boolean, CheckConstraint
)
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.db.session import Base


class TransactionType(str, enum.Enum):
    income = "income"
    expense = "expense"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    amount = Column(Numeric(10, 2), nullable=False)
    type = Column(Enum(TransactionType), nullable=False, index=True)

    category = Column(String, nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)

    notes = Column(Text, nullable=True)

    is_deleted = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    owner = relationship("User", back_populates="transactions")

    __table_args__ = (
        CheckConstraint('amount > 0', name='check_amount_positive'),
    )