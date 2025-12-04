from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(BaseModel):
    title: Optional[str]
    amount: Optional[float]
    category: Optional[str]

class ExpenseOut(ExpenseBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
