import sys

from base import Base


class Sample(Base):
    def __init__(self):
        self.__msg = 'hello'
    

    def test(self):
        print(self.__msg)


def main():
    sample = Sample()
    sample.test()

    # sample2 = Base()

    return 0


if __name__ == '__main__':
    sys.exit(main())
