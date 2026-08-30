class RetrievalEvaluator:

    def __init__(self, retriever):

        self.retriever = retriever

    def evaluate_question(
        self,
        question,
        expected_evidence,
        k
    ):

        results = self.retriever.retrieve(
            question,
            top_k=k
        )

        print("\n" + "=" * 70)

        print("PREGUNTA:")
        print(question)

        print("\nEVIDENCIA ESPERADA:")
        print(expected_evidence)

        print("\nRESULTADOS RECUPERADOS:")

        for i, result in enumerate(
            results,
            start=1
        ):

            print(f"\nResultado {i}")

            print("ID:", result.id)

            print(
                "Distancia:",
                result.distance
            )

            print(
                "Metadata:",
                result.metadata
            )

            print(
                "Texto:",
                result.text[:200]
            )

        print("=" * 70)

        # Comprobar si alguno de los
        # resultados coincide con la
        # evidencia esperada

        for result in results:

            filename = result.metadata.get(
                "filename"
            )

            page = result.metadata.get(
                "page"
            )

            for evidence in expected_evidence:

                if (
                    filename == evidence["filename"]
                    and page == evidence["page"]
                ):

                    return True

        return False

    def evaluate(
        self,
        questions,
        k
    ):

        hits = 0

        for item in questions:

            hit = self.evaluate_question(
                question=item["question"],
                expected_evidence=item[
                    "expected_evidence"
                ],
                k=k
            )

            if hit:
                hits += 1

        total = len(questions)

        hit_rate = (
            hits / total
            if total > 0
            else 0
        )

        return {
            "k": k,
            "hits": hits,
            "total": total,
            "hit_rate": hit_rate
        }