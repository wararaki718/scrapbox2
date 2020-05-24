import optuna
from sklearn.datasets import load_iris

from objective import Objective


def main():
    iris = load_iris()
    X = iris.data
    y = iris.target

    obj = Objective(X, y)

    study = optuna.create_study(direction='maximize')
    study.optimize(obj, n_trials=20)
    print(study.best_trial)
    print('DONE')


if __name__ == '__main__':
    main()
