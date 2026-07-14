from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str

users_db = {}

# Dados de exemplo
users_db["joao123"] = User(username="joao123", email="joao@email.com", password="senha123")
users_db["maria456"] = User(username="maria456", email="maria@email.com", password="senha456")

@app.post("/signup")
def create_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.username] = user
    return {"message": "User created successfully"}

@app.post("/login")
def login(user: User):
    if user.username not in users_db or users_db[user.username].password != user.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}

@app.get("/users")
def list_users():
    return users_db