from pathlib import Path
from app.models.document import Document
from app.ingestion.document_processor import DocumentProcessor
from app.ingestion.text_cleaner import TextCleaner

#Readable document
#pdf = Path("documentos/alabado.pdf")

#OCR - document with image
pdf = Path("documentos/imagen.pdf")
document = Document(
    filename=pdf.name,
    path=str(pdf),
    extension=pdf.suffix
)

processor = DocumentProcessor()
document = processor.process(document)

print("="*60)
print("Archivo:", document.filename)
print("Páginas:", document.pages)

print("="*60)

print(document.text[:200])

print("="*60)
print("Total caracteres:", len(document.text))


print("Documento normalizado")
cleaner = TextCleaner()
texto = cleaner.clean(document.text)
print(texto[:200])