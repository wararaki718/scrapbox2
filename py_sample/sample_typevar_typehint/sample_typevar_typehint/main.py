from typing import Type, TypeVar

from base import Base
from sample import Sample
from sample2 import Sample2

T = TypeVar('T', bound=Base)


def get_item(cls: Type[T]) -> str:
    s = cls()
    return s.get_item()

def main():
    print(get_item(Sample))
    print(get_item(Sample2))
    print('DONE')

if __name__ == '__main__':
    main()
