class Overlap:
    """
        Return last sentence fragment and join with the new chunk.
    """

    def __init__(
        self,
        token_counter,
        overlap_tokens: int
    ):

        self.token_counter = token_counter
        self.overlap_tokens = overlap_tokens

    def apply(self, previous_chunk: str):

        words = previous_chunk.split()
        overlap = []
        current = 0

        for word in reversed(words):

            tokens = self.token_counter.count(word)

            if current + tokens > self.overlap_tokens:
                break

            overlap.insert(0, word)
            current += tokens

        return " ".join(overlap)