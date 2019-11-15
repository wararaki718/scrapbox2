import os


def main():
    print(os.listdir('.'))
    print('copy text.txt to text2.txt.')
    print('')
    with open('text.txt', 'rt') as f1, open('text2.txt', 'wt') as f2:
        for line in f1:
            f2.write(f'hello,{line}')
    print('text2.txt was created.')

    print(os.listdir('.'))
    print('')
    print('show text2.txt:')
    with open('text2.txt', 'rt') as f2:
        for line in f2:
            print(line)
    print('')

    os.remove('text2.txt')
    print('text2.txt was deleted.')
    print(os.listdir('.'))
    print('DONE')


if __name__ == '__main__':
    main()
