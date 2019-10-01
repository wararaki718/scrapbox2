import sys

import numpy as np


def main():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    # data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # error
    print(data)

    d = dict(data)
    print(d)
    return 0


if __name__ == '__main__':
    sys.exit(main())
