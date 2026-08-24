from app.llm.ollama_client import OllamaClient

client = OllamaClient(
    model="llama3.2"
)


prompt = """
Eres un asistente virtual de un museo.
Responde brevemente.
Pregunta:
¿Qué es un museo?
"""

response = client.generate(prompt)

print("=" * 70)
print("RESPUESTA")
print("=" * 70)
print(response)