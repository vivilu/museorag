from pathlib import Path
from app.embeddings.embedding_generator import EmbeddingGenerator
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

generator = EmbeddingGenerator()
document = generator.process(document)

for chunk in document.chunks:

    print(chunk.id)

    print(len(chunk.embedding))

    print(chunk.embedding[:10])