from sklearn.datasets import load_iris
import torch

from my_iterable_dataset import MyIterableDataset
from my_map_dataset import MyMapDataset


def check(dataset: 'Dataset'):
    loader = torch.utils.data.DataLoader(dataset, batch_size=2)
    
    for data in loader:
        print(data)
    print()


def main():
    iris = load_iris()
    X = iris.data[:10, :]

    iter_dataset = MyIterableDataset(X)
    map_dataset = MyMapDataset(X)

    print('check: iterable dataset')
    check(iter_dataset)

    print('check: map dataset')
    check(map_dataset)

    print('DONE')


if __name__ == '__main__':
    main()
