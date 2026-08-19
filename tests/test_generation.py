from app.generation.prompt_builder import PromptBuilder

class RetrievedChunk:

    def __init__(
        self,
        text
    ):

        self.text = text


chunks = [

    RetrievedChunk(
        "La colección arqueológica contiene piezas de la cultura Valdivia."
    ),

    RetrievedChunk(
        "Entre las piezas destacan objetos cerámicos y herramientas."
    ),

    RetrievedChunk(
        "La colección se encuentra en la sala arqueológica."
    )
]


query = "¿Qué piezas arqueológicas tiene el museo?"
builder = PromptBuilder()
prompt = builder.build(
    query=query,
    retrieved_chunks=chunks
)

print("=" * 70)
print(prompt)
print("=" * 70)