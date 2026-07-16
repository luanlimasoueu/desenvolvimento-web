from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
import uvicorn
import json
import os

app = FastAPI()
connected_clients = []


@app.get("/")
async def get_index():
    return FileResponse("index.html")


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    connected_clients.append(ws)

    try:
        while True:
            message = await ws.receive_text()
            reversed_message = message[::-1]

            response_data = {
                "type": "response",
                "message": reversed_message
            }
            await ws.send_text(json.dumps(response_data))
    except:
        connected_clients.remove(ws)


if __name__ == "__main__":
    print("Starting server on http://0.0.0.0:8001")
    print("Open http://localhost:8001 in your browser")
    uvicorn.run(app, host="0.0.0.0", port=8001)