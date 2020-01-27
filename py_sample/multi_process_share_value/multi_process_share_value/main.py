from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Value


def pow(i_range: int) -> int:
    with _Val.get_lock():
        _Val.value += 1
    return _Val.value * _Val.value


def init_globals(val: Value):
    global _Val
    _Val = val


def main():
    val = Value('i', 1)

    with ProcessPoolExecutor(initializer=init_globals, initargs=(val,)) as executer:
        for result in executer.map(pow, range(5)):
            print(result)
    print()


if __name__ == '__main__':
    main()
