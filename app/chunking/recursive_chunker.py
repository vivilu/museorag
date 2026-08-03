from app.chunking.overlap import Overlap
from app.chunking.token_counter import TokenCounter
from collections import deque

class RecursiveChunker:

    def __init__(
        self,
        token_counter: TokenCounter,
        max_tokens: int,
        overlap: Overlap
    ):

        self.token_counter = token_counter
        self.max_tokens = max_tokens
        self.overlap = overlap

        self.separators = [
            "\n\n",
            ". ",
            "; ",
            "\n",
            ": ",
            ", ",
            " "
        ]

    def split(self, sentences):
        pending_sentences = deque(sentences)
        chunks = []
        current_chunk = ""
        current_tokens = 0

        while pending_sentences:

            sentence = pending_sentences.popleft()
            sentence_tokens = self.token_counter.count(sentence)

            # Si la oración es demasiado grande, dividirla
            # e insertarla nuevamente al inicio de la cola
            if sentence_tokens > self.max_tokens:

                fragments = self._split_large_sentence(sentence)

                for fragment in reversed(fragments):
                    pending_sentences.appendleft(fragment)

                continue

            # La oración cabe en el chunk actual
            if (
                current_tokens + sentence_tokens
                <= self.max_tokens
            ):

                if current_chunk:
                    current_chunk += " "
                current_chunk += sentence
                current_tokens += sentence_tokens

            else:
                chunks.append(current_chunk.strip())
                overlap = self.overlap.apply(current_chunk)

                current_chunk = overlap
                current_tokens = self.token_counter.count(overlap)

                if current_chunk:
                    current_chunk += " "
                current_chunk += sentence
                current_tokens += sentence_tokens

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def _split_large_sentence(
        self,
        text
    ):

        # Ya cabe
        if (
            self.token_counter.count(text)
            <= self.max_tokens
        ):

            return [text]

        # Intentar dividir usando distintos separadores
        for separator in self.separators:
            if separator not in text:
                continue

            parts = text.split(separator)
            fragments = []
            current = ""

            for part in parts:
                candidate = (
                    current + separator + part
                    if current
                    else part
                )

                if (
                    self.token_counter.count(candidate)
                    <= self.max_tokens
                ):
                    current = candidate

                else:

                    if current:
                        fragments.append(current.strip())
                    current = part

            if current:
                fragments.append(current.strip())

            result = []

            for fragment in fragments:

                if (
                    self.token_counter.count(fragment)
                    > self.max_tokens
                ):

                    result.extend(
                        self._split_large_sentence(fragment)
                    )

                else:
                    result.append(fragment)

            return result

        return self._fallback_split(text)
        

    def _fallback_split(self, text):

        words = text.split()
        fragments = []
        current = ""

        for word in words:

            candidate = (
                current + " " + word
                if current
                else word
            )

            if self.token_counter.count(candidate) <= self.max_tokens:

                current = candidate

            else:

                fragments.append(current)
                current = word

        if current:
            fragments.append(current)

        return fragments