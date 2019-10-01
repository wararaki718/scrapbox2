import sys

import numpy as np


def main():
    data = np.arange(6).reshape(2, 3)
    print(data)
    for x in np.nditer(data):
        print(x, end=' ')
    print('')

    print(data.T)
    for x in np.nditer(data.T):
        print(x, end=' ')
    print('')
    
    print(data.T)
    for x in np.nditer(data.T.copy()):
        print(x, end=' ')
    print('')

    return 0


if __name__ == '__main__':
    sys.exit(main())
