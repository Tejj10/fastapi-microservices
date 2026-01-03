from fastapi import APIRouter
from app.transport.handlers import say_hello


router = APIRouter()

router.get("/hello")(say_hello)
