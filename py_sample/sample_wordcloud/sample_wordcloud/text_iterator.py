from glob import glob

from bs4 import BeautifulSoup


class TextIterator:
    def __init__(self, dir_path: str, parse_type: str='html.parser', encoding: str='shift-jis'):
        self._dir_path = dir_path
        self._parse_type = parse_type
        self._encoding = encoding

    def _parse(self, file_path: str) -> str:
        with open(file_path, encoding=self._encoding) as f:
            soup = BeautifulSoup(f, self._parse_type, from_encoding=self._encoding)
        try:
            text = soup.find(class_='main_text').text
        except AttributeError:
            text = soup.find('body').text
        
        return text

    def __iter__(self) -> str:
        for file_path in sorted(glob(self._dir_path)):
            text = self._parse(file_path)
            yield text
