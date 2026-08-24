from dataclasses import dataclass, field


@dataclass
class RetrievedChunk:

    id: str

    text: str

    distance: float

    metadata: dict = field(default_factory=dict)