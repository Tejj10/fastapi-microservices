from fastapi import FastAPI
from app.transport.routes import router
from app.store.db import init_db
from app.store.repositories.hello_repo import HelloRepository
from app.business.services.hello_service import HelloService
from app.api.hello_api import HelloAPI

app = FastAPI()
app.include_router(router)

db = init_db()

def get_hello_repo():
    return HelloRepository(db)

def get_hello_service():
    return HelloService(get_hello_repo())

def get_hello_api():
    return HelloAPI(get_hello_service())

app.dependency_overrides[HelloAPI] = get_hello_api
