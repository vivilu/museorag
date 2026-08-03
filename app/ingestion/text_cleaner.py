import re

class TextCleaner:

    def clean_footer(self, text):
        text = re.sub(r'Página\s+\d+\s+de\s+\d+', '', text)
        return text
    
    def clean_pagebreak(self, text):
        text = re.sub(r'\n{2,}', '\n\n', text)
        return text

    def normalize_spaces(self, text):
        return re.sub(r"[ \t]+", " ", text)
    
    def normalize_newlines(self, text):
        return re.sub(r"\n{3,}", "\n\n", text)
    
    def remove_non_printable(self, text):
        return "".join(
            c
            for c in text
            if c.isprintable() or c == "\n"
        )
    
    def normalize_hyphenation(self, text):
        return re.sub(r'(\w)-\n(\w)', r'\1\2', text)
    
    def clean(self, text):
        
        text = self.remove_non_printable(text)
        text = self.normalize_spaces(text)
        text = self.normalize_newlines(text)
        text = self.clean_pagebreak(text)
        text = self.clean_footer(text)
        text = self.normalize_hyphenation(text)
        return text.strip()