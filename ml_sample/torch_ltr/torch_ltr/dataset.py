import numpy as np
import torch


def make_dataset(N_train: int,
                 N_valid: int,
                 D_in: int) -> (torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor):
    weights = torch.randn(D_in, 1)

    X_train = torch.randn(N_train, D_in, requires_grad=True)
    X_valid = torch.randn(N_valid, D_in, requires_grad=True)

    y_train = torch.mm(X_train, weights)
    y_valid = torch.mm(X_valid, weights)

    bins = [-2, -1, 0, 1] # 5 relevances
    y_train = torch.Tensor(
        np.digitize(y_train.clone().detach().numpy(), bins=bins)
    )
    y_valid = torch.Tensor(
        np.digitize(y_valid.clone().detach().numpy(), bins=bins)
    )

    return X_train, X_valid, y_train, y_valid
