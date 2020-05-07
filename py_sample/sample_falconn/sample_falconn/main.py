from falconn import LSHIndex, get_default_parameters
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def main():
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    params = get_default_parameters(X_train.shape[0], X_train.shape[1])
    lsh_index = LSHIndex(params)
    lsh_index.setup(X_train)
    lsh_query = lsh_index.construct_query_object()

    x = X_test[0]
    results = lsh_query.find_k_nearest_neighbors(x, 3)
    print(y_test[0])
    print(results)
    print(y_train[results])

    print('DONE')


if __name__ == '__main__':
    main()
