from typing import List

from janome.tokenizer import Tokenizer


class TextTokenizer:
    def __init__(self):
        self._tokenizer = Tokenizer()

    def __call__(self, text: str) -> List[str]:
        tokens = self._tokenizer.tokenize(text, wakati=True)
        return ' '.join(tokens)
