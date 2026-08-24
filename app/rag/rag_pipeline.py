from app.retrieval.retriever import Retriever
from app.generation.prompt_builder import PromptBuilder
from app.llm.ollama_client import OllamaClient

class RAGPipeline:

    def __init__(
        self,
        retriever,
        prompt_builder,
        llm
    ):

        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm = llm

    def ask(self, query):

        # 1. Recuperar información
        retrieved_chunks = self.retriever.retrieve(
            query
        )

        # 2. Construir prompt
        prompt = self.prompt_builder.build(
            query=query,
            retrieved_chunks=retrieved_chunks
        )

        # 3. Generar respuesta
        response = self.llm.generate(
            prompt
        )

        return response