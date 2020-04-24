from annoy import AnnoyIndex
from sklearn.datasets import load_iris


def main():
    iris = load_iris()
    X = iris.data
    y = iris.target

    dim = X.shape[1]
    t = AnnoyIndex(dim, 'angular')
    
    for i, x in enumerate(X):
        t.add_item(i, x)
    
    n_trees = 10
    t.build(n_trees)

    i_target = 5
    n_nn = 20
    nn_indices = t.get_nns_by_item(i_target, n_nn)
    print('base index               : ', i_target)
    print('base label               : ', y[i_target])
    print('nearest neighbor indices : ', nn_indices)
    print('nearest neighbor labels  : ', y[nn_indices])
    print('DONE')


if __name__ == '__main__':
    main()
