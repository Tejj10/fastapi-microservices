from app.services.ai.service import AIService


class PDFAIAPI:
    def __init__(self, service: AIService):
        self.service = service

    def parse_invoice(self, raw_text: str):
        return self.service.parse(raw_text)
