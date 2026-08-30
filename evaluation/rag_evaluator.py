class RAGEvaluator:

    def __init__(self, rag_pipeline):
        self.rag_pipeline = rag_pipeline

    def evaluate_question(self, question):

        answer = self.rag_pipeline.run(
            question["question"]
        )

        expected = question["answer"]

        return {
            "question": question["question"],
            "expected": expected,
            "answer": answer
        }

    def evaluate(self, questions):

        results = []

        for question in questions:

            result = self.evaluate_question(
                question
            )

            results.append(result)

        return results