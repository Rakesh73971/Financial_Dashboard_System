from pydantic import BaseModel
from typing import List


class SummaryResponse(BaseModel):
    total_income: float
    total_expense: float
    balance: float


class CategorySummary(BaseModel):
    category: str
    total: float


class MonthlySummary(BaseModel):
    month: str
    total: float