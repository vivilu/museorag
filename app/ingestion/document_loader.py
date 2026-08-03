from pathlib import Path
from app.models.document import Document


class DocumentLoader:
    """
        Load PDF file, review document existence and format; return document.
    """

    SUPPORTED_EXTENSIONS = {
        ".pdf"
    }

    def load(self, file_path: str) -> Document:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"No existe el archivo: {file_path}"
            )

        if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Formato no soportado: {path.suffix}"
            )

        return Document(
            filename=path.name,
            path=str(path),
            extension=path.suffix.lower()
        )