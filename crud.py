from sqlalchemy.orm import Session
from models import User, Account, Transaction
from schemas import UserCreate, AccountCreate
from fastapi import HTTPException


def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, password_hash=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_account(db: Session, account: AccountCreate):
    db_account = Account(user_id=account.user_id, account_name=account.account_name, account_type=account.account_type)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def get_accounts_by_user(db: Session, user_id: int):
    return db.query(Account).filter(Account.user_id == user_id).all()

def create_transaction(db: Session, from_account_id: int, to_account_id: int, amount: float):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Transaction amount must be greater than zero")
    if from_account_id == to_account_id:
        raise HTTPException(status_code=400, detail="Cannot transfer money to the same account")
    
    from_account = db.query(Account).filter(Account.id == from_account_id).first()
    to_account = db.query(Account).filter(Account.id == to_account_id).first()

    if not from_account:
        raise HTTPException(status_code=404, detail=f"Source account {from_account_id} not found")

    if not to_account:
        raise HTTPException(status_code=404, detail=f"Destination account {to_account_id} not found")

    if from_account.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds in the source account")

    transaction = Transaction(from_account_id=from_account_id, to_account_id=to_account_id, amount=amount)

    from_account.balance -= amount  
    to_account.balance += amount  

    
    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction
