from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retrieval.retriever import Retriever
from app.embeddings.embedding_generator import EmbeddingModel

# Modelo de embeddings
embedding_model = EmbeddingModel()

# Vector Store
vector_store = ChromaStore()

# Retriever
retriever = Retriever(
    embedding_model=embedding_model,
    vector_store=vector_store,
    top_k=5
)

# Consulta
query = "¿Cuándo se contruyó la casa del alabado?"

# Recuperación
results = retriever.retrieve(query)

# Mostrar resultados
print("=" * 70)

print(
    f"Resultados recuperados: {len(results)}"
)

print("=" * 70)

for i, chunk in enumerate(
    results,
    start=1
):
    print(f"\nResultado {i}")
    print("ID:", chunk.id)
    print("Distancia:", chunk.distance)
    print("Metadata:", chunk.metadata)
    print("Texto:")
    print(chunk.text)
    print("-" * 70)