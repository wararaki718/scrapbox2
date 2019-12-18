from glob import glob
import os
from typing import List

from bs4 import BeautifulSoup
from gensim.models import Word2Vec
from janome.tokenizer import Tokenizer


class TextTokenizer:
    def __init__(self):
        self._tokenizer = Tokenizer()

    def __call__(self, text: str) -> List[str]:
        return self._tokenizer.tokenize(text, wakati=True)


class SentenceIterator:
    def __init__(self, dir_path: str, tokenizer: TextTokenizer=None):
        self._dir_path = dir_path
        if tokenizer:
            self._tokenizer = tokenizer
        else:
            self._tokenizer = lambda x: x.split()

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


class TokensIterator:
    def __init__(self, dir_path: str):
        self._dir_path = dir_path

    def _load_sentences(self, filepath: str) -> List[List[str]]:
        with open(filepath, 'rt') as f:
            return f.readlines()

    def __iter__(self) -> List[str]:
        for filepath in sorted(glob(self._dir_path)):
            sentences = self._load_sentences(filepath)
            for tokens in sentences:
                yield tokens.strip().split()


def store_data(sentences: SentenceIterator,
               store_dir: str='sample_w2v/tokenized',
               threshold: int=100):
    tokens = []
    index = 1
    for sentence in sentences:
        tokens.append(sentence)
        if len(tokens) == threshold:
            filepath = os.path.join(store_dir, f'tokens_{index:03d}.txt')
            with open(filepath, 'wt') as f:
                for token in tokens:
                    f.write(' '.join(token))
                    f.write('\n')
                print(f'{filepath} is created!')
            index += 1
            tokens = []
    
    if tokens:
        filepath = os.path.join(store_dir, f'tokens_{index:03d}.txt')
        with open(filepath, 'wt') as f:
            for token in tokens:
                f.write(' '.join(token))
                f.write('\n')
            print(f'{filepath} is created!')


def main():
    text_tokenizer = TextTokenizer()

    dir_path = 'sample_w2v/data/natsume/files/*.html'
    sentences = SentenceIterator(dir_path, text_tokenizer)

    store_data(sentences)

    dir_path = 'sample_w2v/tokenized/*.txt'
    tokens = TokensIterator(dir_path)

    w2v = Word2Vec(tokens, min_count=10, size=200, iter=5)
    for vocab in w2v.wv.vocab.keys():
        print(vocab)


if __name__ == '__main__':
    main()
