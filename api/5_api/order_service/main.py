import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    product_id: int
    quantity: int

orders_db = []

# Usa variável de ambiente para o host do product_service (funciona local e no Docker)
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://localhost:8002")

@app.post("/order")
def create_order(order: Order):
    response = requests.get(f"{PRODUCT_SERVICE_URL}/product/{order.product_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Product not found")
    product = response.json()

    if product["stock"] < order.quantity:
        raise HTTPException(status_code=400, detail="Not enough stock available")

    orders_db.append(order)
    return {"message": "Order created successfully"}

@app.get("/orders")
def list_orders():
    return orders_db