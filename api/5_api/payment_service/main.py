from fastapi import FastAPI

app = FastAPI()

payments_db = []

# Dados de exemplo
payments_db.append({"order_id": 1, "amount": 7000.00, "status": "completed"})
payments_db.append({"order_id": 2, "amount": 250.00, "status": "pending"})

@app.post("/pay")
def process_payment(amount: float):
    payment = {"amount": amount, "status": "completed"}
    payments_db.append(payment)
    return {"message": "Payment processed successfully", "amount": amount}

@app.get("/payments")
def list_payments():
    return payments_db