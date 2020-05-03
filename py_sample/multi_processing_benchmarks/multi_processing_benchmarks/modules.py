from concurrent import futures

from tqdm import tqdm

from math_functions import math_funcs


def single(X: list):
    for x in tqdm(X):
        for math_func in math_funcs:
            _ = math_func(x)


def multi_threading(X: list):
    with futures.ThreadPoolExecutor() as executer:
        for x in tqdm(X):
            for math_func in math_funcs:
                executers = [
                    executer.submit(math_func, x)
                ]

            for future in futures.as_completed(executers):
                _ = future.result()


def multi_processing(X: list):
    with futures.ProcessPoolExecutor() as executer:
        for x in tqdm(X):
            for math_func in math_funcs:
                executers = [
                    executer.submit(math_func, x)
                ]
            
            for future in futures.as_completed(executers):
                _ = future.result()
