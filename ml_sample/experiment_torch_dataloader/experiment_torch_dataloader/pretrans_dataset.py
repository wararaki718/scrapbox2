from typing import Tuple

import torch
from torch.utils.data import Dataset


class PreTransDataset(Dataset):
    def __init__(self, X: 'numpy.ndarray', y: 'numpy.ndarray', transformer: 'PCA'):
        self._X = transformer.transform(X)
        self._y = y
    
    def __len__(self) -> int:
        return self._X.shape[0]

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        x = self._X[idx, :]
        return torch.Tensor(x).float(), torch.Tensor(self._y[idx, :]).long()
