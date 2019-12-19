from glob import glob
import os
import re
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
    def __init__(self, dir_path: str):
        self._dir_path = dir_path

    def _load_text(self, filepath: str, encoding: str='shift-jis') -> str:
        with open(filepath, encoding=encoding) as f:
            soup = BeautifulSoup(f, from_encoding=encoding, features='html.parser')

        try:
            text = soup.find(class_='main_text').text
        except AttributeError:
            text = soup.find('body').text

        return text
    
    def __iter__(self) -> str:
        for filepath in sorted(glob(self._dir_path)):
            text = self._load_text(filepath)
            sentences = re.split(r'。|\n|\r', text)
            for sentence in sentences:
                yield sentence


class CorpusIterator:
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


def write_data2text(tokens: List[str], filepath: str):
    with open(filepath, 'wt') as f:
        for token in tokens:
            f.write(' '.join(token))
            f.write('\n')
        print(f'{filepath} is created!')


def main():
    dir_path = 'sample_w2v/data/natsume/files/*.html'
    sentences = SentenceIterator(dir_path)

    tokenizer = TextTokenizer()

    dir_path='sample_w2v/tokenized'
    index = 1
    corpora = []
    chunksize = 100000
    for sentence in sentences:
        tokens = tokenizer(sentence)
        if not tokens:
            continue

        corpora.append(tokens)
        if len(corpora) == chunksize:
            filepath = os.path.join(dir_path, f'corpora_{index:03d}.txt')
            write_data2text(corpora, filepath)
            corpora = []
            index += 1

    if corpora:
        filepath = os.path.join(dir_path, f'corpora_{index:03d}.txt')
        write_data2text(corpora, filepath)

    dir_path = 'sample_w2v/tokenized/*.txt'
    corpora = CorpusIterator(dir_path)

    w2v = Word2Vec(corpora, min_count=10, size=200, iter=5)
    for vocab in w2v.wv.vocab.keys():
        print(vocab)


if __name__ == '__main__':
    main()
