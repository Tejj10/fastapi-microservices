from app.services.ai.repo import AIRepository
from app.services.ai.service import AIService
from app.api.pdf_ai_api import PDFAIAPI


def get_ai_repo():
    return AIRepository()


def get_ai_service():
    return AIService(get_ai_repo())


def get_pdf_ai_api():
    return PDFAIAPI(get_ai_service())
