import json

from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retrieval.retriever import Retriever
from app.generation.prompt_builder import PromptBuilder
from app.llm.ollama_client import OllamaClient
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
prompt_builder = PromptBuilder()
llm = OllamaClient(
    model="llama3.2"
)

# ----------------------------------------
# RAG Pipeline
# ----------------------------------------
rag_pipeline = RAGPipeline(
    retriever=retriever,
    prompt_builder=prompt_builder,
    llm=llm
)

# ----------------------------------------
# Evaluador
# ----------------------------------------
evaluator = RAGEvaluator(
    rag_pipeline
)

# ----------------------------------------
# Ejecutar evaluación
# ----------------------------------------
results = evaluator.evaluate(
    questions
)

# ----------------------------------------
# Mostrar resultados
# ----------------------------------------
for index, result in enumerate(
    results,
    start=1
):

    print("=" * 70)
    print(f"RESULTADO {index}")
    print("=" * 70)
    print("PREGUNTA:")
    print(result["question"])
    print("\nRESPUESTA ESPERADA:")
    print(result["expected"])
    print("\nRESPUESTA GENERADA:")
    print(result["answer"])
    print(
        f"\nSIMILITUD SEMÁNTICA: "
        f"{result['semantic_score']:.4f}"
    )
    print(
        f"RESULTADO: "
        f"{'CORRECTA' if result['correct'] else 'INCORRECTA'}"
    )
    print()

total = len(results)
correct = sum(
    1
    for result in results
    if result["correct"]
)

accuracy = correct / total if total > 0 else 0

print("=" * 70)
print("EVALUACIÓN SEMÁNTICA DEL RAG")
print("=" * 70)
print(f"Preguntas evaluadas: {total}")
print(f"Respuestas correctas: {correct}")
print(f"Respuestas incorrectas: {total - correct}")
print(f"Accuracy: {accuracy:.2%}")