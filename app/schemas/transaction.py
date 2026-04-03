from pydantic import BaseModel, Field
from datetime import date as Date
from typing import Optional
from enum import Enum


class TransactionType(str, Enum):
    income = "income"
    expense = "expense"


class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0)
    type: TransactionType
    category: str
    date: Date
    notes: Optional[str] = None


class TransactionUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0)
    type: Optional[TransactionType] = None
    category: Optional[str] = None
    date: Optional[Date] = None
    notes: Optional[str] = None


class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: TransactionType
    category: str
    date: Date
    notes: Optional[str]

    class Config:
        from_attributes = True