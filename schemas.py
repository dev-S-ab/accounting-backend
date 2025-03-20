from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  


class AccountCreate(BaseModel):
    user_id: int
    account_name: str = Field(..., min_length=3, max_length=100)
    account_type: Optional[str] = None  


class AccountResponse(BaseModel):
    id: int
    user_id: int
    account_name: str
    account_type: Optional[str] = None
    balance: float
    created_at: datetime

    class Config:
        from_attributes = True


class TransactionCreate(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float = Field(..., gt=0)  


class TransactionResponse(BaseModel):
    id: int
    from_account_id: int
    to_account_id: int
    amount: float
    timestamp: datetime

    class Config:
        from_attributes = True
