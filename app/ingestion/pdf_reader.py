import pymupdf

class PDFReader:

    def read(self, pdf_path: str):
        """
        Read an pdf document and return its content.
        """

        pages_text = []

        with pymupdf.open(pdf_path) as doc:

            for page in doc:
                pages_text.append(
                    page.get_text("text").strip()
                )

        text = "\n".join(pages_text)

        return text, len(pages_text)