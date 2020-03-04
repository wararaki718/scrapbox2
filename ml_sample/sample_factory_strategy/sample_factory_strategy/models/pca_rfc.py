from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from .base import BaseModel


class PcaRfc(BaseModel):
    def __init__(self):
        self._pipeline = Pipeline([
            ('pca', PCA(n_components=2)),
            ('rfc', RandomForestClassifier())
        ])

    def fit(self, X: 'np.ndarray', y: 'np.ndarray') -> 'np.ndarray':
        self._pipeline.fit(X, y)
        return self._pipeline
    
    def score(self, X: 'np.ndarray', y: 'np.ndarray') -> 'np.ndarray':
        return self._pipeline.score(X, y)
