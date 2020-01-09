import numpy as np


def main():
    A = np.array([[6, 2], [2, 3]])

    Lambda, V = np.linalg.eig(A)

    Q = np.diag(Lambda)

    V_inv = np.linalg.inv(V)

    result = V.dot(Q).dot(V_inv)
    print(result)


if __name__ == '__main__':
    main()
