from fastapi import FastAPI
from app.transport.routes import router

app = FastAPI(title="PDF Parsing Microservice")

app.include_router(router)

