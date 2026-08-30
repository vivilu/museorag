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
        text, pages, pages_text = self.pdf_reader.read(document.path)

        # Without enought text, use OCR
        if len(text.strip()) < 50:
            text, pages, pages_text = self.ocr_reader.read(
                document.path
            )

        # Clean texto
        cleaned_pages = []

        for page_text in pages_text:

            cleaned_text = self.cleaner.clean(
                page_text
            )

            cleaned_pages.append(
                cleaned_text
            )

        text = "\n".join(cleaned_pages)

        # Update documento
        document.text = text
        document.pages = pages
        document.page_texts = pages_text

        return document