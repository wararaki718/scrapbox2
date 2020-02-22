from argparse import ArgumentParser
import os

import xgboost as xgb


def parse_options():
    parser = ArgumentParser()
    parser.add_argument("--data-dir", dest="data_dir", default="../data")
    parser.add_argument("--model-path", dest="model_path", default="../model/model.bin")

    return parser.parse_args()


def main():
    options = parse_options()
    
    dtrain = xgb.DMatrix(os.path.join(options.data_dir, 'agaricus.txt.train'))
    dtest = xgb.DMatrix(os.path.join(options.data_dir, 'agaricus.txt.test'))

    params = {
        'max_depth': 2,
        'eta': 1,
        'objective': 'binary:logistic'
    }
    n_round = 2

    print('train:')
    booster = xgb.train(params, dtrain, n_round)
    preds = booster.predict(dtest)
    print(preds)

    print('test:')
    booster.save_model(options.model_path)
    print('DONE')


if __name__ == '__main__':
    main()
