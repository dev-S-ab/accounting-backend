from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from db import get_db

router = APIRouter()

@router.post("/users/")
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/users/")
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)
