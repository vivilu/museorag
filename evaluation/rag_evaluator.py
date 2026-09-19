from evaluation.semantic_evaluator import SemanticEvaluator

class RAGEvaluator:

    def __init__(self, rag_pipeline):
        self.rag_pipeline = rag_pipeline
        self.semantic_evaluator = SemanticEvaluator()

    def evaluate_question(self, question):
        answer = self.rag_pipeline.ask(
            question["question"]
        )

        expected = question["expected_answer"]

        semantic_result = self.semantic_evaluator.evaluate(
            expected=expected,
            generated=answer
        )

        return {
            "id": question["id"],
            "question": question["question"],
            "expected": expected,
            "answer": answer,
            "semantic_score": semantic_result["score"],
            "correct": semantic_result["correct"]
        }

    def evaluate(self, questions):

        results = []

        for question in questions:

            result = self.evaluate_question(
                question
            )

            results.append(result)

        return results