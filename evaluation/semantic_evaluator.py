import numpy as np

from app.embeddings.embedding_model import EmbeddingModel


class SemanticEvaluator:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

    def similarity(
        self,
        expected,
        generated
    ):

        expected_embedding = self.embedding_model.encode(expected)
        generated_embedding = self.embedding_model.encode(generated)
        expected_embedding = np.array(expected_embedding)
        generated_embedding = np.array(generated_embedding)

        similarity = np.dot(
            expected_embedding,
            generated_embedding
        )

        return float(similarity)

    def evaluate(
        self,
        expected,
        generated,
        threshold=0.80
    ):

        score = self.similarity(
            expected,
            generated
        )

        correct = score >= threshold

        return {
            "score": score,
            "correct": correct
        }