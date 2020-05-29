from sklearn.datasets import load_iris

from config import Config
from model import Classifier
from predictor import Predictor


def main():
    # config
    config_path = 'config.yml'
    config = Config.load(config_path=config_path)

    # load datasets
    iris = load_iris()
    X = iris.data
    y = iris.target

    # create model
    model = Classifier()
    model.fit(X, y)
    model.save(config.model_path)

    # prediciton
    predictor = Predictor.load(config)
    preds = predictor(X[:10, :])
    print(preds)
    print(preds.shape)
    print('DONE')


if __name__ == '__main__':
    main()
    