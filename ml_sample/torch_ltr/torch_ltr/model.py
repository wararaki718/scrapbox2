import torch


class Net(torch.nn.Module):
    def __init__(self, D_in: int, D_out: int, H: int=10):
        super(Net, self).__init__()
        self.l1 = torch.nn.Linear(D_in, H)
        self.l2 = torch.nn.Linear(H, D_out)
    
    def forward(self, x: torch.Tensor):
        x = torch.sigmoid(self.l1(x))
        x = self.l2(x)
        return x
