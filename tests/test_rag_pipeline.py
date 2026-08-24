from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retrieval.retriever import Retriever
from app.generation.prompt_builder import PromptBuilder
from app.llm.ollama_client import OllamaClient
from app.rag.rag_pipeline import RAGPipeline

# ----------------------------------------
# Embedding Model
# ----------------------------------------
embedding_model = EmbeddingModel()

# ----------------------------------------
# Vector Store
# ----------------------------------------
vector_store = ChromaStore()

# ----------------------------------------
# Retriever
# ----------------------------------------
retriever = Retriever(
    embedding_model=embedding_model,
    vector_store=vector_store,
    top_k=5
)

# ----------------------------------------
# Prompt Builder
# ----------------------------------------
prompt_builder = PromptBuilder()

# ----------------------------------------
# LLM
# ----------------------------------------
llm = OllamaClient(model="llama3.2")

# ----------------------------------------
# RAG Pipeline
# ----------------------------------------
rag = RAGPipeline(
    retriever=retriever,
    prompt_builder=prompt_builder,
    llm=llm
)

# ----------------------------------------
# Consulta
# ----------------------------------------
query = "¿Cuándo se contruyó la casa del alabado?"

# ----------------------------------------
# Ejecutar RAG
# ----------------------------------------
response = rag.ask(query)

# ----------------------------------------
# Mostrar respuesta
# ----------------------------------------
print("=" * 70)
print("PREGUNTA")
print("=" * 70)
print(query)
print("\n")
print("=" * 70)
print("RESPUESTA")
print("=" * 70)
print(response)
print("=" * 70)