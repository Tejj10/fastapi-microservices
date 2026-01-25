import re

class AIService:


    def parse_invoice(self, text: str) -> dict:
        data = {}

        # Invoice Number
        invoice_no = re.search(r"(Invoice\s*No\.?|Invoice\s*#)\s*[:\-]?\s*(\S+)", text, re.IGNORECASE)
        if invoice_no:
            data["invoice_number"] = invoice_no.group(2)

        # Date
        date = re.search(r"(Date)\s*[:\-]?\s*([0-9\/\-]+)", text, re.IGNORECASE)
        if date:
            data["invoice_date"] = date.group(2)

        # Total Amount
        total = re.search(r"(Total|Grand Total)\s*[:\-]?\s*₹?\s*([0-9,.]+)", text, re.IGNORECASE)
        if total:
            data["total_amount"] = total.group(2)

        # Vendor name (simple heuristic)
        lines = text.splitlines()
        if lines:
            data["vendor"] = lines[0].strip()

        return {
            "document_type": "invoice",
            "extracted_fields": data,
            "confidence": "rule-based"
        }
