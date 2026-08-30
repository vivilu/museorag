from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from tests.test_generation import RetrievedChunk
from app.models.retrieved_chunk import RetrievedChunk


class Retriever:

    def __init__(
        self,
        embedding_model,
        vector_store,
        top_k=7
    ):

        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.top_k = top_k

    def retrieve(self, query, top_k=None):


        if top_k is None:
            top_k = self.top_k

        query_embedding = self.embedding_model.encode(
            query
        )

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        retrieved_chunks = []

        for i in range(len(results["ids"][0])):

            retrieved_chunk = RetrievedChunk(
                id=results["ids"][0][i],
                text=results["documents"][0][i],
                distance=results["distances"][0][i],
                metadata=results["metadatas"][0][i]
            )

            retrieved_chunks.append(
                retrieved_chunk
            )

        return retrieved_chunks
