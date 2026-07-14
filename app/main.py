from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello from Cloud Run!",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "local")
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }