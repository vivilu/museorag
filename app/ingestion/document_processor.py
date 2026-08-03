from app.models.document import Document

from app.ingestion.pdf_reader import PDFReader
from app.ingestion.ocr_reader import OCRReader
from app.ingestion.text_cleaner import TextCleaner


class DocumentProcessor:

    def __init__(self):

        self.pdf_reader = PDFReader()
        self.ocr_reader = OCRReader()
        self.cleaner = TextCleaner()

    def process(self, document: Document) -> Document:

        # Extract texto
        text, pages = self.pdf_reader.read(document.path)

        # Without enought text, use OCR
        if len(text.strip()) < 50:
            text = self.ocr_reader.read(document.path)

        # Clean texto
        text = self.cleaner.clean(text)

        # Update documento
        document.text = text
        document.pages = pages

        return document