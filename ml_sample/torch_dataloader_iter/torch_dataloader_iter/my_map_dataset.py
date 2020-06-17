import torch


class MyMapDataset(torch.utils.data.Dataset):
    def __init__(self, X: 'numpy.ndarray'):
        self._X = X

    def __len__(self):
        return self._X.shape[0]

    def __getitem__(self, idx: int) -> torch.Tensor:
        return torch.Tensor(self._X[idx, :])
