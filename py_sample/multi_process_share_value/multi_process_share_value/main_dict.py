from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import Manager


def pow(data: dict) -> dict:
    print(f'call_powfunc: {data}')
    data['id'] += 1
    data['score'] *= 2
    return data


def main():
    with Manager() as manager:
        data = manager.dict({'id': 1, 'score': 2.0})
        print(type(data))

        with ProcessPoolExecutor() as executer:
            executers = [
                executer.submit(pow, data) for _ in range(10)
            ]
            for future in as_completed(executers):
                result = future.result()
                print(f'as_completed: {result}')


if __name__ == '__main__':
    main()
