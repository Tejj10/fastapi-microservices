from app.services.ai.service import AIService

class PDFAIAPI:
    def __init__(self):
        self.service = AIService()

    def parse(self, raw_text: str):
        return self.service.parse_invoice(raw_text)


