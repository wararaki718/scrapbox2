import random
import time

from modules import single
from modules import multi_threading
from modules import multi_processing

def check(func, X):
    start = time.time()
    func(X)
    end = time.time()
    print(f"{func.__name__}: {end-start}")


def main():
    random.seed(42)
    N = 100000
    X = [random.random() for _ in range(N)]

    check(single, X)
    check(multi_threading, X)
    check(multi_processing, X)

    print('DONE')


if __name__ == '__main__':
    main()
