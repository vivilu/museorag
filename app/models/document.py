from dataclasses import dataclass, field
from pathlib import Path

from app.models.chunk import Chunk

@dataclass
class Document:
    """
    Types of atributes from document.
    """
    filename: str
    path: str
    extension: str
    text: str = ""
    pages: int = 0
    chunks: list[Chunk] = field(default_factory=list)

    # Texto separado por página
    page_texts: list[str] = field(
        default_factory=list
    )

    # Chunks generados
    chunks: list[Chunk] = field(
        default_factory=list
    )