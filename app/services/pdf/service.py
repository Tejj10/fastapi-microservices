import pdfplumber

class PDFService:
    def extract_text(self, file):
        text = ""

        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        return {
            "filename": file.filename,
            "characters": len(text),
            "preview": text[:300],
            "full_text": text
        }
