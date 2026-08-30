import json

from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retrieval.retriever import Retriever

from evaluation.retrieval_evaluator import RetrievalEvaluator

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

# ----------------------------------------
# Evaluador
# ----------------------------------------
evaluator = RetrievalEvaluator(
    retriever
)

# ----------------------------------------
# Evaluar diferentes K
# ----------------------------------------
K_VALUES = [1, 3, 5, 7, 9]
for k in K_VALUES:
    result = evaluator.evaluate(
        questions=questions,
        k=k
    )

    print(
        f"K={result['k']} | "
        f"Hits={result['hits']}/"
        f"{result['total']} | "
        f"Hit Rate={result['hit_rate']:.2%}"
    )