from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retrieval.retriever import Retriever
from app.generation.prompt_builder import PromptBuilder
from app.llm.ollama_client import OllamaClient

# ----------------------------------------
# 1. Embedding Model
# ----------------------------------------
embedding_model = EmbeddingModel()

# ----------------------------------------
# 2. Vector Store
# ----------------------------------------
vector_store = ChromaStore()

# ----------------------------------------
# 3. Retriever
# ----------------------------------------
retriever = Retriever(
    embedding_model=embedding_model,
    vector_store=vector_store,
    top_k=5
)

# ----------------------------------------
# 4. Prompt Builder
# ----------------------------------------
prompt_builder = PromptBuilder()

# ----------------------------------------
# 5. LLM
# ----------------------------------------
llm = OllamaClient(model="llama3.2")

# ----------------------------------------
# 6. Pregunta
# ----------------------------------------
query = "¿Cuándo se contruyó la casa del alabado?"

# ----------------------------------------
# 7. Retrieval
# ----------------------------------------
retrieved_chunks = retriever.retrieve(query)

print("=" * 70)
print("CHUNKS RECUPERADOS")
print("=" * 70)

for i, chunk in enumerate(
    retrieved_chunks,
    start=1
):
    print(f"\nChunk {i}")
    print("ID:", chunk.id)
    print("Distancia:", chunk.distance)
    print("Texto:", chunk.text)

# ----------------------------------------
# 8. Construir prompt
# ----------------------------------------
prompt = prompt_builder.build(
    query=query,
    retrieved_chunks=retrieved_chunks
)
print("\n")
print("=" * 70)
print("PROMPT")
print("=" * 70)
print(prompt)

# ----------------------------------------
# 9. Generar respuesta
# ----------------------------------------
response = llm.generate(prompt)
print("\n")
print("=" * 70)
print("RESPUESTA")
print("=" * 70)
print(response)