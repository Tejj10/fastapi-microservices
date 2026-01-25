from fastapi import UploadFile, File, Depends
from app.api.pdf_api import PDFApi

def say_hello():
    return {"message": "Hello World"}

def parse_pdf(
    file: UploadFile = File(...),
    api: PDFApi = Depends()
):
    return api.parse(file)
