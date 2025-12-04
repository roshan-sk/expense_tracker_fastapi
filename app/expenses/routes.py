from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.db.database import get_db
from app.expenses.schemas import ExpenseCreate, ExpenseOut, ExpenseUpdate
from app.expenses.models import Expense
from app.auth.deps import get_current_user

router = APIRouter(prefix="/expenses", tags=["Expenses"])

# Get all expenses for current user
@router.get("/", response_model=List[ExpenseOut])
def get_expenses(user = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Expense).filter(Expense.user_id == user.id).all()

# Create a new expense
@router.post("/", response_model=ExpenseOut)
def create_expense(expense: ExpenseCreate, user = Depends(get_current_user), db: Session = Depends(get_db)):
    new_expense = Expense(
        **expense.dict(),
        user_id=user.id,
        date=datetime.now()
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

# Update expense
@router.put("/{expense_id}", response_model=ExpenseOut)
def update_expense(expense_id: int, data: ExpenseUpdate, user = Depends(get_current_user), db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == user.id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    for field, value in data.dict(exclude_unset=True).items():
        setattr(expense, field, value)
    db.commit()
    db.refresh(expense)
    return expense

# Delete expense
@router.delete("/{expense_id}")
def delete_expense(expense_id: int, user = Depends(get_current_user), db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == user.id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted successfully"}
