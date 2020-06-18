from sklearn.datasets import load_iris
import torch

from my_dataset import MyDataset


def check(dataset: 'MyDataset'):
    ## this is not running, because iterator object does not allow shuffle=True.
    loader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=True)

    for data in loader:
        print(data)
    print()


def main():
    iris = load_iris()
    X = iris.data[:10, :]

    my_dataset = MyDataset(X)

    for i in range(1, 6, 1):
        print(f'{i}-th check:')
        check(my_dataset)
    
    print('DONE')


if __name__ == '__main__':
    main()
