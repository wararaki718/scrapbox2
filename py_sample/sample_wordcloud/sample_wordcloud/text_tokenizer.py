from typing import List

from janome.tokenizer import Tokenizer


class TextTokenizer:
    def __init__(self):
        self._tokenizer = Tokenizer()
    
    def __call__(self, text: str) -> List[str]:
        tokens = self._tokenizer.tokenize(text, stream=True)
        return [token.surface for token in tokens if '名詞' in token.part_of_speech]
