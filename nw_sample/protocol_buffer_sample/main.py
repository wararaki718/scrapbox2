import sys
import os

import sample_pb2


FILENAME = 'item.data'


def main():
    # create item
    item = sample_pb2.Item()
    item.id = 1
    item.name = 'test'
    print('create item info:')
    print(item)

    # serialize the item
    print(f'before : {os.listdir(".")}')
    with open(FILENAME, 'wb') as f:
        f.write(item.SerializeToString())
    print(f'after  : {os.listdir(".")}')

    # read serialized data
    item2 = sample_pb2.Item()
    with open(FILENAME, 'rb') as f:
        item2.ParseFromString(f.read())
    print('parsed item info:')
    print(item2)

    print('delete binary file.')
    os.remove(FILENAME)
    print('DONE')

    return 0


if __name__ == '__main__':
    sys.exit(main())
