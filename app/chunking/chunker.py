from app.chunking.sentence_splitter import SentenceSplitter
from app.chunking.token_counter import TokenCounter
from app.chunking.overlap import Overlap
from app.chunking.recursive_chunker import RecursiveChunker

from app.models.chunk import Chunk
from config.settings import MAX_TOKENS, OVERLAP_TOKENS


class Chunker:

    def __init__(
        self,
        max_tokens: int = MAX_TOKENS,
        overlap_tokens: int = OVERLAP_TOKENS
    ):

        self.token_counter = TokenCounter()
        self.sentence_splitter = SentenceSplitter()
        self.overlap = Overlap(
            token_counter=self.token_counter,
            overlap_tokens=overlap_tokens
        )
        self.recursive_chunker = RecursiveChunker(
            token_counter=self.token_counter,
            max_tokens=max_tokens,
            overlap=self.overlap
        )

    def process(self, document):

        sentences = self.sentence_splitter.split(
            document.text
        )

        chunks = self.recursive_chunker.split(
            sentences
        )

        document.chunks = []

        for index, chunk_text in enumerate(chunks):

            chunk = Chunk(
                id=index,
                text=chunk_text,
                page=0,
                token_count=self.token_counter.count(chunk_text)
            )

            document.chunks.append(chunk)

        return document