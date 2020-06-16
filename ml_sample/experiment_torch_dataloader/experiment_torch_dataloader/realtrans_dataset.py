from typing import Tuple

import torch
from torch.utils.data import Dataset


class RealTransDataset(Dataset):
    def __init__(self, X: 'numpy.ndarray', y: 'numpy.ndarray', transformer: 'PCA'):
        self._X = X
        self._y = y
        self._transformer = transformer
    
    def __len__(self) -> int:
        return self._X.shape[0]

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        x = self._transformer.transform([self._X[idx]])
        return torch.Tensor(x), torch.Tensor([self._y[idx, :]]).long()
