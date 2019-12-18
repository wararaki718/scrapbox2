from glob import glob
from typing import List

from bs4 import BeautifulSoup
from gensim.models import Word2Vec
from janome.tokenizer import Tokenizer


class TextTokenizer:
    def __init__(self):
        self._tokenizer = Tokenizer()

    def __call__(self, text: str) -> List[str]:
        return self._tokenizer.tokenize(text, wakati=True)


class TextDataset:
    def __init__(self, dir_path: str, tokenizer: TextTokenizer=None):
        self._dir_path = dir_path
        if tokenizer:
            self._tokenizer = tokenizer
        else:
            self._tokenizer = lambda x: x

    def _load_text(self, filepath: str, encoding: str='shift-jis') -> str:
        with open(filepath, encoding=encoding) as f:
            soup = BeautifulSoup(f, from_encoding=encoding, features='html.parser')

        try:
            text = soup.find(class_='main_text').text
        except AttributeError:
            text = soup.find('body').text

        return text

    def __iter__(self) -> List[str]:
        for filepath in sorted(glob(self._dir_path)):
            text = self._load_text(filepath)
            yield self._tokenizer(text)


def main():
    text_tokenizer = TextTokenizer()

    dir_path = 'sample_w2v/data/natsume/files/*.html'
    text_dataset = TextDataset(dir_path, text_tokenizer)

    w2v = Word2Vec(text_dataset, min_count=10, size=200)
    for vocab in w2v.wv.vocab.keys():
        print(vocab)


if __name__ == '__main__':
    main()
