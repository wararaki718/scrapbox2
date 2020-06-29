import glob
import re


def show(items: list):
    for item in items:
        print(item)
    print()

def main():
    data_paths = glob.glob('data/*.txt')

    print('before:')
    show(data_paths)

    regex = r'2020-01-(0[2-9]|1[0-9])'
    results = list(filter(lambda x: re.search(regex, x) is not None, data_paths))

    print('after')
    show(results)

    print('DONE')


if __name__ == '__main__':
    main()
