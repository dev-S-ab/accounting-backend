from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from db import get_db

router = APIRouter()

@router.post("/accounts/")
def add_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    return crud.create_account(db, account)

@router.get("/users/{user_id}/accounts/")
def get_user_accounts(user_id: int, db: Session = Depends(get_db)):
    return crud.get_accounts_by_user(db, user_id)
