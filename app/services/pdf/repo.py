import fitz

class PDFRepository:
    def extract_text(self, pdf_bytes):
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
