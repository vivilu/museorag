import chromadb

class ChromaStore:

    def __init__(
        self,
        persist_directory="data/chroma"
    ):

        self.client = chromadb.PersistentClient(
            path=persist_directory
        )

        self.collection = self.client.get_or_create_collection(
            name="museo"
        )

    def add_document(self, document):

        ids = []
        embeddings = []
        documents = []
        metadatas = []

        for chunk in document.chunks:

            ids.append(
                f"{document.filename}_{chunk.id}"
            )

            embeddings.append(
                chunk.embedding
            )

            documents.append(
                chunk.text
            )

            metadatas.append({
                "filename": document.filename,
                "page": chunk.page,
                "chunk_id": chunk.id
            })


            print("\n" + "=" * 70)
            print("CHROMA STORE")
            print("Documento:", document.filename)
            print("IDs:", len(ids))
            print("Embeddings:", len(embeddings))
            print("Documents:", len(documents))
            print("Metadatas:", len(metadatas))

            if embeddings:
                print(
                    "Primer embedding:",
                    type(embeddings[0]),
                    len(embeddings[0])
                )

            print("=" * 70)

        self.collection.upsert(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results