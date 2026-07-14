from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

products_db = {}

# Dados de exemplo
products_db[1] = Product(id=1, name="Notebook", price=3500.00, stock=10)
products_db[2] = Product(id=2, name="Mouse sem fio", price=50.00, stock=100)
products_db[3] = Product(id=3, name="Teclado mecânico", price=250.00, stock=30)

@app.post("/product")
def create_product(product: Product):
    if product.id in products_db:
        raise HTTPException(status_code=400, detail="Product already exists")
    products_db[product.id] = product
    return {"message": "Product created successfully"}

@app.get("/product/{product_id}")
def get_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]

@app.get("/products")
def list_products():
    return products_db