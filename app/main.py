from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "application": os.getenv("APP_NAME"),
        "environment": os.getenv("ENVIRONMENT"),
        "version": os.getenv("VERSION"),
        "hostname": socket.gethostname(),
        "secret_loaded": os.getenv("API_KEY") is not None
    }
    
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/service")
def service():
    return {
        "status": "running"
    }