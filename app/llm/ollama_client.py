import ollama

class OllamaClient:

    def __init__(self, model="llama3.2"):

        self.model = model

    def generate(self, prompt):

        response = ollama.generate(
            model=self.model,
            prompt=prompt
        )

        return response["response"]