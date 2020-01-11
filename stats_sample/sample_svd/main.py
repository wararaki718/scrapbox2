import numpy as np


def show_matrix(val: np.array, name: str):
    print(name)
    print(val)
    print()


def main():
    print('base matrix')
    A = np.array([[7, 2, -1, 3], [3, 4, 5, 10], [5, 3, 6, 8]])
    show_matrix(A, 'A')

    # svd
    U, Sigma, V = np.linalg.svd(A)

    print('show decomposed components')
    show_matrix(U, 'U')
    show_matrix(Sigma, 'Sigma')
    show_matrix(V, 'V')

    # reduce dimensions
    print('the results of dimentionality reduction')
    for k in range(3, 0, -1):
        result = U[:, :k].dot(np.diag(Sigma[:k])).dot(V[:k, :])
        show_matrix(result, f'k={k}')

    return


if __name__ == '__main__':
    main()
