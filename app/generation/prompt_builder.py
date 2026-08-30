class PromptBuilder:

    def build(
        self,
        query,
        retrieved_chunks
    ):

        context_parts = []

        for i, chunk in enumerate(
            retrieved_chunks,
            start=1
        ):

            context_parts.append(
                f"[Contexto {i}]\n"
                f"{chunk.text}"
            )

        context = "\n\n".join(
            context_parts
        )

        prompt = f"""
Eres un asistente virtual de un museo.

Responde la pregunta del usuario utilizando únicamente la información proporcionada en el
contexto.

Si la información necesaria para responder no se encuentra en el contexto, indica que
no dispones de información suficiente.

No inventes información.

Contexto:

{context}

Pregunta:

{query}

Respuesta:
""".strip()

        return prompt