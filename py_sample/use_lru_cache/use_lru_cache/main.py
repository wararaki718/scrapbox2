from functools import lru_cache
import random
import time

@lru_cache(maxsize=128)
def calc_used_lru_cache(x: int) -> int:
    result = 0
    for i in range(x*10):
        result += i
    return result


def calc(x: int) -> int:
    result = 0
    for i in range(x*10):
        result += i
    return result


def main():
    X = [random.randrange(1, 128) for i in range(10000)]
    start_tm = time.time()
    _ = list(map(calc, X))
    end_tm = time.time()
    print(f'calc: {end_tm-start_tm} sec')

    start_tm = time.time()
    _ = list(map(calc_used_lru_cache, X))
    end_tm = time.time()
    print(f'use lru_cache: {end_tm-start_tm} sec')

    print('DONE')


if __name__ == '__main__':
    main()
