# tools.py

import os
from pypdf import PdfReader


class FinancialDocumentTool:
    @staticmethod
    def read_data_tool(path: str):
        """
        Read text from a PDF file
        """
        if not os.path.exists(path):
            return "File not found."

        try:
            reader = PdfReader(path)
            text = ""

            for page in reader.pages:
                content = page.extract_text()
                if content:
                    text += content + "\n"

            return text.strip()

        except Exception as e:
            return f"Error reading PDF: {str(e)}" 