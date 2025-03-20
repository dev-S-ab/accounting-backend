from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
from db import get_db

router = APIRouter()

@router.post("/transactions/")
def transfer_money(from_account_id: int, to_account_id: int, amount: float, db: Session = Depends(get_db)):
    return crud.create_transaction(db, from_account_id, to_account_id, amount)
