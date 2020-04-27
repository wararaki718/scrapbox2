from collections import Counter

from annoy import AnnoyIndex
import numpy as np
from sklearn.base import BaseEstimator


class NNClassifier(BaseEstimator):
    def __init__(self,
                 metric: str='angular',
                 n_trees: int=10,
                 n_neighbors: int=5,
                 search_k: int=-1):
        self._metric = metric
        self._n_trees = n_trees
        self._n_neighbors = n_neighbors
        self._search_k = search_k
        self._train_y = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        if isinstance(X, list):
            X = np.array(X)
        elif not isinstance(X, np.ndarray):
            X = X.toarray()
        
        self._model = AnnoyIndex(X.shape[1], self._metric)
        for i, x in enumerate(X):
            self._model.add_item(i, x)
        
        if isinstance(y, list):
            y = np.array(y)
        elif not isinstance(y, np.ndarray):
            y = y.toarray()

        self._train_y = y
        self._model.build(self._n_trees)

    def predict(self, X: np.ndarray) -> np.ndarray:
        if isinstance(X, list):
            X = np.array(X)
        elif not isinstance(X, np.ndarray):
            X = X.toarray()
        y = np.apply_along_axis(self._predict, axis=1, arr=X)
        return y

    def _predict(self, x: np.ndarray) -> str:
        nn_indices = self._model.get_nns_by_vector(x, self._n_neighbors, search_k=self._search_k)
        nn_labels = self._train_y[nn_indices]
        counter = Counter(nn_labels)
        most_common = counter.most_common(1)
        return most_common[0][0]

    def get_params(self, deep=True):
        return {
            'metric': self._metric,
            'n_trees': self._n_trees,
            'n_neighbors': self._n_neighbors,
            'search_k': self._search_k
        }