import faiss
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def main():
    iris = load_iris()
    X = iris.data.astype('float32')
    n_dim = X.shape[1]

    index = faiss.IndexFlatL2(n_dim)
    print(index.is_trained)

    X_train, X_test = train_test_split(X)

    index.add(X_train)
    print(index.ntotal)

    k = 4
    distances, nn_indices = index.search(X_train[:5], k)
    print('sanity check:')
    print(nn_indices)
    print(distances)
    print()

    distances, nn_indices = index.search(X_test, k)
    print('search:')
    print(nn_indices[:5])
    print(distances[:5])

    print('DONE')


if __name__ == '__main__':
    main()
