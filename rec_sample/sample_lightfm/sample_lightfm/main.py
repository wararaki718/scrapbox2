import numpy as np
from lightfm import LightFM
from lightfm.evaluation import precision_at_k, auc_score
from lightfm.datasets import fetch_movielens


def main():
    movielens = fetch_movielens()

    train = movielens['train']
    print(type(train))
    print(train)
    test = movielens['test']
    print(type(test))
    print(test)

    model = LightFM(learning_rate=0.05, loss='bpr')
    model.fit(train, epochs=10)

    train_precision = precision_at_k(model, train, k=10).mean()
    test_precision = precision_at_k(model, test, k=10, train_interactions=train).mean()

    train_auc = auc_score(model, train).mean()
    test_auc = auc_score(model, test, train_interactions=train).mean()

    print(f'train precision: {train_precision}')
    print(f'test precision: {test_precision}')

    print(f'train auc: {train_auc}')
    print(f'test auc: {test_auc}')
    print('DONE')


if __name__ == '__main__':
    main()
