from sample import Sample


def main():
    s = Sample()

    print(s.call(1))
    print(s.call('1'))
    print(s.call(1.0))

    print('DONE')


if __name__ == '__main__':
    main()
