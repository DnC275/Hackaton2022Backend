from fastapi import FastAPI
from app.routers import (
    upload,
    process
)

app = FastAPI()

app.include_router(upload.router)
app.include_router(process.router)
