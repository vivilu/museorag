from dataclasses import dataclass, field


@dataclass
class Chunk:
    """
    Types of atributes from chunk.
    """

    id: int
    text: str
    page: int = 0
    token_count: int = 0
    title: str = ""
    tokens: int = 0
    embedding: list[float] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)