import numpy as np
from sklearn.datasets import load_boston


def _sigmoid(x: np.array) -> np.array:
    return 1.0 / (1 + np.exp(-x))


def logistic_regression(features: np.array,
                        target: np.array,
                        n_iter: int = 100,
                        learning_rate: float = 0.001) -> np.array:
    
    weights = np.zeros(features.shape[1])

    for _ in range(n_iter):
        x = np.dot(features, weights)
        y = _sigmoid(x)

        gradients = np.dot(features.T, target - y) / y.shape[0]
        weights -= learning_rate * gradients
    
    return weights


def log_likelihood(features: np.array,
                   target: np.array,
                   weights: np.array) -> np.array:
    y = np.dot(features, weights)
    likelihood = np.sum(target * y - np.log(1 + np.exp(y)))
    return likelihood


def main():

    boston = load_boston()
    X = boston.data
    y = boston.target

    weights = logistic_regression(X, y)
    print(weights.shape)
    print(X.shape)
    print(y.shape)

    likelihood = log_likelihood(X, y, weights)
    print(likelihood)
    print('DONE')


if __name__ == '__main__':
    main()
