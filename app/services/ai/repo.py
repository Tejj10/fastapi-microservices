import re
from typing import Dict, List


class AIRepository:
    def parse_invoice(self, raw_text: str) -> Dict:
        text = raw_text.replace("\n", " ")

        return {
            "invoice_number": self._extract_invoice_number(text),
            "invoice_date": self._extract_date(text),
            "vendor_name": self._extract_vendor(text),
            "customer_name": self._extract_customer(text),
            "items": self._extract_items(raw_text),
            "subtotal": self._extract_amount("subtotal", text),
            "tax": self._extract_amount("tax", text),
            "total": self._extract_amount("total", text),
            "currency": self._extract_currency(text)
        }

    def _extract_invoice_number(self, text: str):
        match = re.search(r"(invoice\s*(no|number)?[:\s]*)(\w+)", text, re.I)
        return match.group(3) if match else None

    def _extract_date(self, text: str):
        match = re.search(r"\b(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})\b", text)
        return match.group(1) if match else None

    def _extract_vendor(self, text: str):
        match = re.search(r"(from|vendor)[:\s]*([A-Za-z\s]+)", text, re.I)
        return match.group(2).strip() if match else None

    def _extract_customer(self, text: str):
        match = re.search(r"(to|bill to)[:\s]*([A-Za-z\s]+)", text, re.I)
        return match.group(2).strip() if match else None

    def _extract_amount(self, label: str, text: str):
        match = re.search(rf"{label}[:\s]*([\d,.]+)", text, re.I)
        return match.group(1) if match else None

    def _extract_currency(self, text: str):
        if "₹" in text or "INR" in text:
            return "INR"
        if "$" in text or "USD" in text:
            return "USD"
        if "€" in text or "EUR" in text:
            return "EUR"
        return None

    def _extract_items(self, raw_text: str) -> List[Dict]:
        items = []
        lines = raw_text.split("\n")

        for line in lines:
            match = re.search(r"(.+?)\s+(\d+)\s+([\d,.]+)", line)
            if match:
                items.append({
                    "description": match.group(1).strip(),
                    "quantity": int(match.group(2)),
                    "price": match.group(3)
                })

        return items


