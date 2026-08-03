from pathlib import Path

from app.models.document import Document

from app.ingestion.document_processor import DocumentProcessor

from app.chunking.chuncker import Chunker


# Crear documento
pdf = Path("documentos/alabado.pdf")
document = Document(
    filename=pdf.name,
    path=str(pdf),
    extension=pdf.suffix
)

# Procesar documento
processor = DocumentProcessor()
document = processor.process(document)

# Chunking
chunker = Chunker()
document = chunker.process(document)

print("=" * 70)
print(f"Documento: {document.filename}")
print(f"Páginas: {document.pages}")
print(f"Número de chunks: {len(document.chunks)}")
print("=" * 70)

for chunk in document.chunks:
    print(f"\nChunk {chunk.id}")
    print(f"Tokens: {chunk.token_count}")
    print("-" * 50)
    print(chunk.text[:300])
    print("-" * 50)