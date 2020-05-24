import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score


class Objective:
    def __init__(self, X: np.ndarray, y: np.ndarray):
        self._X = X
        self._y = y

    def __call__(self, trial: 'optuna.trial.Trial'):
        params = {
            'C': trial.suggest_loguniform('C', 0.05, 1.0)
        }
        model = LogisticRegression(**params)

        score = cross_val_score(model, self._X, self._y, n_jobs=-1, cv=3)
        accuracy = score.mean()
        return accuracy
