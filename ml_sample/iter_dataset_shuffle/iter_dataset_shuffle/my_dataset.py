import torch


class MyDataset(torch.utils.data.IterableDataset):
    def __init__(self, X: 'numpy.ndarray'):
        super(MyDataset).__init__()
        self._X = X

    def __iter__(self) -> torch.Tensor:
        for i in range(self._X.shape[0]):
            yield torch.Tensor(self._X[i, :])
