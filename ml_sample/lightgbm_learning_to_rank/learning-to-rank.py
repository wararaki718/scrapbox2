import lightgbm as lgbm
import pandas as pd
from sklearn.datasets import load_svmlight_files
from scipy.stats import spearmanr


def main():
    x_train, y_train, x_test, y_test = load_svmlight_files(
        ['data/rank.train', 'data/rank.test']
    )
    train_query = pd.read_csv('data/rank.train.query', header=None).values.flatten()

    model = lgbm.LGBMRanker(
        num_leaves=50,
        n_estimators=200,
        random_state=42
    )
    print(model)
    model.fit(
        x_train, y_train, 
        group=train_query, 
        eval_metric='ndgc',
        eval_at=[1, 3 ,5]
    )
    preds = model.predict(x_test)

    print(spearmanr(y_test, preds))
    print('DONE')


if __name__ == '__main__':
    main()
