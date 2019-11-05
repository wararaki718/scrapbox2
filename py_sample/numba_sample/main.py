from numba import jit
import random
import time


@jit(nopython=True)
def monte_carlo_pi_with_numba(n_sample: int) -> float:
    acc = 0
    for _ in range(n_sample):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / n_sample


def monte_carlo_pi_without_numba(n_sample: int) -> float:
    acc = 0
    for _ in range(n_sample):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / n_sample


def main():
    n = 1000
    print('Not use numba')
    random.seed(42)
    start_tm = time.time()
    monte_carlo_pi_without_numba(n)
    end_tm = time.time()
    print(f'spend time: {end_tm - start_tm}')
    print()

    print('use numba')
    random.seed(42)
    start_tm = time.time()
    monte_carlo_pi_with_numba(n)
    end_tm = time.time()
    print(f'spend time: {end_tm - start_tm}')
    print()

    print('use numba (2)')
    random.seed(42)
    start_tm = time.time()
    monte_carlo_pi_with_numba(n)
    end_tm = time.time()
    print(f'spend time: {end_tm - start_tm}')

    return 0


if __name__ == '__main__':
    main()
