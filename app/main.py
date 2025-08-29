# app/main.py
from fastapi import FastAPI
from .router import router # Import the router from router.py


app = FastAPI(title="VIT Full Stack Challenge API")


app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Server is running", "operation_code": 1}