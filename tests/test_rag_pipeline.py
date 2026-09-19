from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retrieval.retriever import Retriever
from app.llm.ollama_client import OllamaClient
from app.generation.prompt_builder import PromptBuilder
from app.rag.rag_pipeline import RAGPipeline

# ----------------------------------------
# Componentes
# ----------------------------------------
embedding_model = EmbeddingModel()
vector_store = ChromaStore()
retriever = Retriever(
    embedding_model=embedding_model,
    vector_store=vector_store
)
prompt_builder = PromptBuilder()
llm = OllamaClient(model="llama3.2")

# ----------------------------------------
# RAG Pipeline
# ----------------------------------------
rag = RAGPipeline(
    retriever=retriever,
    prompt_builder = prompt_builder,
    llm=llm
)

# ----------------------------------------
# Pregunta
# ----------------------------------------
query = (
    "¿Cuándo se construyó la casa del alabado?"
)

# ----------------------------------------
# Ejecutar
# ----------------------------------------
answer = rag.ask(query)

print("=" * 70)
print("PREGUNTA")
print(query)

print("=" * 70)
print("RESPUESTA")
print(answer)