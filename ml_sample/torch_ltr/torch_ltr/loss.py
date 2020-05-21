import torch


def pairwise_loss(s_i: float,
                  s_j: float,
                  S_ij: int,
                  sigma: float = 1.0) -> float:
    C = torch.log1p(torch.exp(-sigma * (s_i - s_j)))

    if S_ij == -1:
        C += sigma * (s_i - s_j)
    elif S_ij == 0:
        C += 0.5 * sigma * (s_i - s_j)
    elif S_ij == 1:
        pass
    else:
        raise ValueError("S_ij: -1/0/1")
    return C
