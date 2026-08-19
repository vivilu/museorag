from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retrieval.retriever import Retriever

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
for i, document in enumerate(
    results["documents"][0]
):

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