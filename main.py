from fastapi import FastAPI
from routes import users, accounts, transactions

app = FastAPI()

app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(transactions.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Accounting API"}
