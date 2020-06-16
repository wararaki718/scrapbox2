import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

from pretrans_dataset import PreTransDataset
from realtrans_dataset import RealTransDataset
from train import train


def main():
    iris = load_iris()
    X = iris.data
    y = iris.target
    y = np.zeros((len(iris.target), 1 + iris.target.max()), dtype=int)
    y[np.arange(len(iris.target)), iris.target] = 1
    print(y.shape)

    pca = PCA(n_components=2)
    pca.fit(X)

    rdataset = RealTransDataset(X, y, pca)
    pdataset = PreTransDataset(X, y, pca)

    train(rdataset)
    train(pdataset)

    print('DONE')


if __name__ == '__main__':
    main()
