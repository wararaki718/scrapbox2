import joblib
import numpy as np
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

class Classifier:
    def __init__(self):
        self._model = Pipeline([
            ('pca', PCA()),
            ('rfc', RandomForestClassifier())
        ])
        params = {
            "pca__n_components": [2, 3],
            "rfc__criterion": ['gini', 'entropy'],
            "rfc__n_estimators": [10, 50, 100],
            "rfc__max_depth": [None, 2, 3, 5]
        }
        self._grid_search_cv = GridSearchCV(
            estimator=self._model,
            param_grid=params,
            cv=5,
            n_jobs=-1
        )
    
    def fit(self, X: np.ndarray, y: np.ndarray):
        self._grid_search_cv.fit(X, y)
        self._model = self._grid_search_cv.best_estimator_
    
    def save(self, model_path: str):
        joblib.dump(self._model, model_path)
