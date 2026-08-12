from app.embeddings.embedding_model import EmbeddingModel

class EmbeddingGenerator:

    def __init__(self):
        self.model = EmbeddingModel()

    def process(self, document):

        for chunk in document.chunks:
            chunk.embedding = self.model.encode(
                chunk.text
            )

        return document