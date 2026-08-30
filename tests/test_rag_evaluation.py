import json

from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retrieval.retriever import Retriever

from app.generation.generator import Generator
from app.rag.rag_pipeline import RAGPipeline

from evaluation.rag_evaluator import RAGEvaluator

# ----------------------------------------
# Cargar preguntas
# ----------------------------------------
with open(
    "evaluation/questions.json",
    "r",
    encoding="utf-8"
) as file:

    questions = json.load(file)

# ----------------------------------------
# Componentes
# ----------------------------------------
embedding_model = EmbeddingModel()
vector_store = ChromaStore()
retriever = Retriever(
    embedding_model=embedding_model,
    vector_store=vector_store
)
generator = Generator()

# ----------------------------------------
# RAG Pipeline
# ----------------------------------------
rag_pipeline = RAGPipeline(
    retriever=retriever,
    generator=generator
)

# ----------------------------------------
# Evaluador
# ----------------------------------------
evaluator = RAGEvaluator(rag_pipeline)

# ----------------------------------------
# Evaluación
# ----------------------------------------
results = evaluator.evaluate(questions)

# ----------------------------------------
# Mostrar resultados
# ----------------------------------------
for index, result in enumerate(results, start=1):

    print("=" * 70)
    print(f"PREGUNTA {index}")
    print("Pregunta:", result["question"])
    print("RESPUESTA ESPERADA:")
    print(result["expected"])
    print("RESPUESTA GENERADA:")
    print(result["answer"])