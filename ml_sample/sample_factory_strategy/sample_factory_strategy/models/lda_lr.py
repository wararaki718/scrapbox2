from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from .base import BaseModel


class LdaLr(BaseModel):
    def __init__(self):
        self._pipeline = Pipeline([
            ('lda', LinearDiscriminantAnalysis(n_components=2)),
            ('lr', LogisticRegression())
        ])
    
    def fit(self, X: 'np.ndarray', y: 'np.ndarray') -> 'np.ndarray':
        self._pipeline.fit(X, y)
        return self._pipeline
    
    def score(self, X: 'np.ndarray', y: 'np.ndarray') -> 'np.ndarray':
        return self._pipeline.score(X, y)
