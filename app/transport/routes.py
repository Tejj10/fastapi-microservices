from fastapi import APIRouter
from app.transport.handlers import say_hello, parse_pdf

router = APIRouter()

router.get("/hello")(say_hello)
router.post("/parse-pdf")(parse_pdf)




