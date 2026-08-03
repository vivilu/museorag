from transformers import AutoTokenizer

class TokenCounter:
    """
        Count tokens. Use model BAAI/bge-m3 the same tokenizer for the same chunks - consistency.
    """

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "BAAI/bge-m3",
            trust_remote_code=True
    )

    def count(self, text: str) -> int:

        return len(
            self.tokenizer.encode(
                text,
                add_special_tokens=False
            )
        )