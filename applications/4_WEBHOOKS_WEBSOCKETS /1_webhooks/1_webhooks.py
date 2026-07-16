from fastapi import FastAPI, Request, HTTPException
import uvicorn

app = FastAPI()

def verify_signature(body: bytes, signature: str) -> bool:
    return True

@app.post("/webhook/payment")
async def payment_webhook(request: Request):
    body = await request.body()
    signature = request.headers.get("Stripe-Signature")

    if not verify_signature(body, signature):
        raise HTTPException(status_code=400, detail="Invalid signature")

    payload = await request.json()

    if payload["type"] == "payment_intent.succeeded":
        print("Payment succeeded:", payload["data"]["id"])

    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)