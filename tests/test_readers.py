from app.ingestion.pdf_reader import PDFReader
from app.ingestion.ocr_reader import OCRReader

path = "documentos/evaluacion/exposiciones.pdf"

# ----------------------------------------
# PDF Reader
# ----------------------------------------
pdf_reader = PDFReader()
text, pages, pages_text = pdf_reader.read(path)

print("=" * 70)
print("PDF READER")
print("=" * 70)
print("Páginas:", pages)
print("Page texts:", len(pages_text))
print("Caracteres:", len(text))

if pages_text:
    print("Primera página:")
    print(pages_text[0][:300])

# ----------------------------------------
# OCR Reader
# ----------------------------------------
ocr_reader = OCRReader()
text, pages, pages_text = ocr_reader.read(path)

print("\n")
print("=" * 70)
print("OCR READER")
print("=" * 70)
print("Páginas:", pages)
print("Page texts:", len(pages_text))
print("Caracteres:", len(text))

if pages_text:
    print("Primera página:")
    print(pages_text[0][:300])
