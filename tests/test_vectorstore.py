from pathlib import Path

from app.models.document import Document

from app.ingestion.document_processor import DocumentProcessor
from app.chunking.chunker import Chunker
from app.embeddings.embedding_generator import EmbeddingGenerator
from app.vectorstore.chroma_store import ChromaStore


# ----------------------------------------
# 1. Crear Document
# ----------------------------------------

pdf = Path("documentos/alabado.pdf")

document = Document(
    filename=pdf.name,
    path=str(pdf),
    extension=pdf.suffix
)


# ----------------------------------------
# 2. Ingestion
# ----------------------------------------

processor = DocumentProcessor()

document = processor.process(document)


# ----------------------------------------
# 3. Chunking
# ----------------------------------------

chunker = Chunker()

document = chunker.process(document)


print("Chunks generados:", len(document.chunks))


# ----------------------------------------
# 4. Embeddings
# ----------------------------------------

embedding_generator = EmbeddingGenerator()

document = embedding_generator.process(document)


print(
    "Dimensión embedding:",
    len(document.chunks[0].embedding)
)


# ----------------------------------------
# 5. VectorStore
# ----------------------------------------

store = ChromaStore()

store.add_document(document)

print("Documento almacenado correctamente.")


# ----------------------------------------
# 6. Verificar ChromaDB
# ----------------------------------------

print(
    "Elementos almacenados:",
    store.collection.count()
)