from app.services.pdf.service import PDFService
from app.api.pdf_ai_api import PDFAIAPI

class PDFApi:
    def __init__(self):
        self.pdf_service = PDFService()
        self.ai_api = PDFAIAPI()

    def parse(self, file):
        pdf_result = self.pdf_service.extract_text(file)
        ai_result = self.ai_api.parse(pdf_result["full_text"])

        return {
            "pdf": pdf_result,
            "ai": ai_result
        }
