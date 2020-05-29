import joblib
import numpy as np

from config import Config
from model import Classifier

class Predictor:
    def __init__(self, model: Classifier):
        self.model = model

    def __call__(self, X: np.ndarray) -> np.ndarray:
        return self.predict(X)

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.predict(X)

    @classmethod
    def load(cls, config: Config) -> 'Predictor':
        model = joblib.load(config.model_path)
        return Predictor(model=model)
