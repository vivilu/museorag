import pymupdf

class PDFReader:

    def read(self, pdf_path: str):
        """
        Read an pdf document and return its content.
        """

        pages_text = []

        with pymupdf.open(pdf_path) as doc:

            for page in doc:
                
                page_text = page.get_text(
                    "text"
                ).strip()

                pages_text.append(
                    page_text
                )

        text = "\n".join(pages_text)

        return (
            text,
            len(pages_text),
            pages_text
        )