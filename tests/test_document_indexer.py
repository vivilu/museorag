from app.ingestion.document_processor import DocumentProcessor
from app.chunking.chunker import Chunker
from app.embeddings.embedding_generator import EmbeddingGenerator
from app.vectorstore.chroma_store import ChromaStore

from app.indexing.document_indexer import DocumentIndexer

# ----------------------------------------
# Componentes
# ----------------------------------------
document_processor = DocumentProcessor()
chunker = Chunker()
embedding_generator = EmbeddingGenerator()
vector_store = ChromaStore()

# ----------------------------------------
# Indexador
# ----------------------------------------
indexer = DocumentIndexer(
    document_processor=document_processor,
    chunker=chunker,
    embedding_generator=embedding_generator,
    vector_store=vector_store
)

# ----------------------------------------
# Procesar documentos
# ----------------------------------------
indexer.index_directory(
    "documentos/evaluacion"
)

# ----------------------------------------
# Verificar
# ----------------------------------------
print("\n" + "=" * 70)
print(
    "Total de elementos en ChromaDB:",
    vector_store.collection.count()
)
print("=" * 70)