import spacy

class SentenceSplitter:
    """
        Split text in sentences.
    """

    def __init__(self):
        self.nlp = spacy.load("es_core_news_md")

    def split(self, text: str):
        doc = self.nlp(text)

        return [
            sent.text.strip()
            for sent in doc.sents
            if sent.text.strip()
        ]