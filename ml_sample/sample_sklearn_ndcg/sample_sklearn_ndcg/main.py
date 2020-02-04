from lightfm import LightFM
from lightfm.datasets import fetch_movielens
from lightfm.evaluation import auc_score, precision_at_k
from sklearn.metrics import ndcg_score


def main():
    movielens = fetch_movielens()

    train = movielens['train']
    test = movielens['test']
    print(train.shape)
    print(test.shape)

    model = LightFM(learning_rate=0.05, loss='bpr')
    model.fit(train, epochs=10)

    k = 10
    train_precision = precision_at_k(model, train, k=k).mean()
    test_precision = precision_at_k(model, test, k=k).mean()
    print(f'precision_at_{k}(train): {train_precision}')
    print(f'precision_at_{k}(test) : {test_precision}')

    train_auc = auc_score(model, train).mean()
    test_auc = auc_score(model, test).mean()
    print(f'auc_score(train): {train_auc}')
    print(f'auc_score(test) : {test_auc}')

    y_train_preds = model.predict_rank(train)
    y_test_preds = model.predict_rank(test)
    train_ndcg = ndcg_score(train.toarray(), y_train_preds.toarray())
    test_ndcg = ndcg_score(test.toarray(), y_test_preds.toarray())
    print(f'ndcg_score(train): {train_ndcg}')
    print(f'ndcg_score(test) : {test_ndcg}')

    print('DONE')

    return 0


if __name__ == '__main__':
    main()
