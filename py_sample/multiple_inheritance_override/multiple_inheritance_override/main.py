class Base1:
    def func(self):
        print('Base')


class Base2:
    def func(self):
        print('Base2')


class Sample(Base1, Base2):
    def test(self):
        print('test')


def main():
    sample = Sample()
    sample.func()
    print('DONE')


if __name__ == '__main__':
    main()
