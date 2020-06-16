import torch
import torch.nn as nn
import torch.nn.functional as F


class NNModel(nn.Module):
    def __init__(self, n_input: int, n_output: int, n_hidden: int=64):
        super(NNModel, self).__init__()
        self.layer1 = nn.Linear(n_input, n_hidden)
        self.layer2 = nn.Linear(n_hidden, n_hidden)
        self.layer3 = nn.Linear(n_hidden, n_output)

    def forward(self, x: 'torch.Tensor') -> 'torch.Tensor':
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return torch.squeeze(F.softmax(x), dim=1)
