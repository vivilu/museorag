from typing import List


class RecursiveChunker:

    def __init__(self, token_counter):
        self.token_counter = token_counter
        self.separators = [
            "\n\n",
            ". ",          
            "; ",
            "\n",
            ", ",
            " "
        ]

    def split(
        self,
        text: str,
        max_tokens: int
    ) -> List[str]:

        # Caso base
        if self.token_counter.count(text) <= max_tokens:

            return [text.strip()]

        # Intentar dividir usando distintos separadores
        for separator in self.separators:

            if separator not in text:
                continue

            parts = text.split(separator)
            chunks = []
            current = ""

            for part in parts:

                candidate = (
                    current + separator + part
                    if current
                    else part
                )

                if self.token_counter.count(candidate) <= max_tokens:
                    current = candidate

                else:

                    if current:
                        chunks.append(current.strip())
                    current = part

            if current:
                chunks.append(current.strip())

            # Procesar recursivamente cualquier fragmento que siga siendo grande
            final_chunks = []

            for chunk in chunks:

                if self.token_counter.count(chunk) > max_tokens:
                    final_chunks.extend(
                        self.split(
                            chunk,
                            max_tokens
                        )
                    )

                else:
                    final_chunks.append(chunk)
            return final_chunks

        # Último recurso:
        # dividir palabra por palabra

        words = text.split()
        chunks = []
        current = ""

        for word in words:
            candidate = (
                current + " " + word
                if current
                else word
            )

            if self.token_counter.count(candidate) <= max_tokens:
                current = candidate

            else:
                chunks.append(current)
                current = word

        if current:
            chunks.append(current)
        return chunks