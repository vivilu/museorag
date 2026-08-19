from app.vectorstore.chroma_store import ChromaStore
from app.embeddings.embedding_model import EmbeddingModel

# Modelo de embeddings
embedding_model = EmbeddingModel()

# VectorStore
store = ChromaStore()

# Pregunta
query = "¿Cuándo se contruyó la casa del alabado?"

# Embedding de la pregunta
query_embedding = embedding_model.encode(query)

# Búsqueda
results = store.search(
    query_embedding,
    top_k=5
)

# Mostrar resultados
for i, document in enumerate(results["documents"][0]):
    print("=" * 70)
    print(f"Resultado {i + 1}")
    print("-" * 70)
    print(document)
    print()
    print(
        "Distancia:",
        results["distances"][0][i]
    )
    print(
        "Metadata:",
        results["metadatas"][0][i]
    )