import pymupdf
import easyocr
from PIL import Image
import numpy as np


class OCRReader:

    def __init__(self):

        self.reader = easyocr.Reader(
            ['es'],
            gpu=False
        )

    def read(self, pdf_path: str):

        pages_text = []

        with pymupdf.open(pdf_path) as doc:

            for page in doc:

                pix = page.get_pixmap(dpi=300)

                image = Image.frombytes(
                    "RGB",
                    (pix.width, pix.height),
                    pix.samples
                )

                image = np.array(image)
                results = self.reader.readtext(image)
                page_text = []

                for _, text, confidence in results:

                    if confidence >= 0.60:

                        page_text.append(text)

                # Guardar el texto de esta página
                pages_text.append(
                    " ".join(page_text)
                )

        # Unir todas las páginas
        text = "\n".join(pages_text)

        return (
            text,
            len(pages_text),
            pages_text
        )