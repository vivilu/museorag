from pathlib import Path
from app.models.document import Document

class DocumentIndexer:

    def __init__(
        self,
        document_processor,
        chunker,
        embedding_generator,
        vector_store
    ):
        self.document_processor = document_processor
        self.chunker = chunker
        self.embedding_generator = embedding_generator
        self.vector_store = vector_store

    def index_directory(self, directory):

        directory = Path(directory)

        pdf_files = list(
            directory.glob("*.pdf")
        )

        print(
            f"Documentos encontrados: {len(pdf_files)}"
        )

        for pdf_path in pdf_files:

            print(
                f"\nProcesando: {pdf_path.name}"
            )

            document = Document(
                filename=pdf_path.name,
                path=str(pdf_path),
                extension=pdf_path.suffix
            )

            # 1. Ingestion
            document = self.document_processor.process(
                document
            )

            # 2. Chunking
            document = self.chunker.process(
                document
            )

            # 3. Embeddings
            document = self.embedding_generator.process(
                document
            )

            print("\n" + "=" * 70)

            print("DOCUMENTO:", document.filename)
            print("PÁGINAS:", document.pages)
            print("PAGE_TEXTS:", len(document.page_texts))
            print("CHUNKS:", len(document.chunks))

            if document.chunks:

                print(
                    "PRIMER CHUNK:",
                    document.chunks[0].text[:100]
                )

                print(
                    "PRIMER CHUNK PAGE:",
                    document.chunks[0].page
                )

                print(
                    "PRIMER EMBEDDING TYPE:",
                    type(document.chunks[0].embedding)
                )

                print(
                    "PRIMER EMBEDDING LENGTH:",
                    len(document.chunks[0].embedding)
                )

            print("=" * 70)

            # 4. Vector Store
            self.vector_store.add_document(
                document
            )

            print(
                f"Chunks indexados: "
                f"{len(document.chunks)}"
            )