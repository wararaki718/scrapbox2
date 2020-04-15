from glob import glob
from typing import Tuple

from news import News


class NewsIterator:
    def __init__(self, dir_path: str):
        self._dir_path = dir_path

    def _parse(self, file_path: str) -> News:
        with open(file_path) as f:
            lines = [line.replace('　', '').strip() for line in f if line is not None]
        url = lines[0]
        date_time = lines[1]
        title = lines[2]
        content = ''.join(lines[3:])
        label = file_path.split('/')[1]
        return News(url=url, date_time=date_time, title=title, content=content, label=label)

    def __iter__(self) -> News:
        for file_path in sorted(glob(self._dir_path)):
            if 'LICENSE' in file_path:
                print(f'skip "{file_path}"')
                continue

            news = self._parse(file_path)
            yield news
