import numpy as np


def show_eigen(A: np.array):
    w, v = np.linalg.eig(A)
    print('eigenvalue: ', w)
    print('vector    : ', v)
    print('')


def main():
    A = np.array([[1, 0], [0, 2]])
    show_eigen(A)

    B = np.array([[2, 1], [2, 3]])
    show_eigen(B)

    C = np.array([[6, -3, -7], [-1, 2, 1], [5, -3, -6]])
    show_eigen(C)


if __name__ == '__main__':
    main()
