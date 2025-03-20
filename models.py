from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from db import Base,engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    accounts = relationship("Account", back_populates="user")

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    account_name = Column(String, unique=True, index=True, nullable=False)
    account_type = Column(String, nullable=True)
    balance = Column(Float, default=0.0)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="accounts")
    sent_transactions = relationship("Transaction", foreign_keys="[Transaction.from_account_id]", back_populates="from_account")
    received_transactions = relationship("Transaction", foreign_keys="[Transaction.to_account_id]", back_populates="to_account")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    from_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    to_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    from_account = relationship("Account", foreign_keys=[from_account_id], back_populates="sent_transactions")
    to_account = relationship("Account", foreign_keys=[to_account_id], back_populates="received_transactions")
Base.metadata.create_all(bind=engine)