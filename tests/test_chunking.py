from pathlib import Path

from app.models.document import Document

from app.ingestion.document_processor import DocumentProcessor

from app.chunking.chunker import Chunker


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

"""
#Print: text of chunk, # tokens
for chunk in document.chunks:
    print(f"\nChunk {chunk.id}")
    print(f"Tokens: {chunk.token_count}")
    print("-" * 50)
    print(chunk.text[:300])
    print("-" * 50)
"""

"""
#Print: overlap
for i in range(len(document.chunks)-1):
    print("="*70)
    print("FINAL CHUNK")
    print(document.chunks[i].text[-200:])
    print()
    print("INICIO SIGUIENTE")
    print(document.chunks[i+1].text[:200])
"""

"""
#Print: overlap
for chunk in document.chunks:
    print(chunk.text[-10:])
"""

print()
print("ID | TOKENS | CARACTERES")
print("-"*40)

for chunk in document.chunks:

    print(
        f"{chunk.id:02} | "
        f"{chunk.token_count:03} | "
        f"{len(chunk.text)}"
    )