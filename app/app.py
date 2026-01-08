from fastapi import FastAPI

from app.transport.routes import router
from app.api.hello_api import HelloAPI
from app.services.hello.repo import HelloRepository
from app.services.hello.service import HelloService

app = FastAPI()
app.include_router(router)

hello_repo = HelloRepository()
hello_service = HelloService(hello_repo)

def get_hello_api():
    return HelloAPI(hello_service)

app.dependency_overrides[HelloAPI] = get_hello_api

