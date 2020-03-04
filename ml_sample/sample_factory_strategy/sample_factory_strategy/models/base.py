from sklearn.base import BaseEstimator


class BaseModel(BaseEstimator):
    def fit(self, X: 'np.ndarray', y: 'np.ndarray') -> 'np.ndarray':
        raise NotImplementedError

    def score(self, X: 'np.ndarray', y: 'np.ndarray') -> 'np.ndarray':
        raise NotImplementedError
