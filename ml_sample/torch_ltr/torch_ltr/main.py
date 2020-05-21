from argparse import ArgumentParser

import numpy as np
import torch
import torch.optim as optim

from dataset import make_dataset
from loss import pairwise_loss
from model import Net


def parse_args():
    parser = ArgumentParser()
    
    parser.add_argument('--n-train', dest='n_train', type=int, default=500)
    parser.add_argument('--n-valid', dest='n_valid', type=int, default=100)
    parser.add_argument('--n-input', dest='n_input', type=int, default=50)
    parser.add_argument('--n-output', dest='n_output', type=int, default=1)
    parser.add_argument('--n-epoch', dest='n_epoch', type=int, default=10)
    parser.add_argument('--n-batch', dest='n_batch', type=int, default=16)
    parser.add_argument('--n-sampling', dest='n_sampling', type=int, default=50)

    return parser.parse_args()


def swapped_pairs(y_preds: torch.Tensor, y_target: torch.Tensor):
    N = y_target.shape[0]
    swapped = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (y_target[i] < y_target[j] and y_preds[i] > y_preds[j]) or \
               (y_target[i] > y_target[j] and y_preds[i] < y_preds[j]):
                swapped += 1
    return swapped


def main():
    options = parse_args()

    N_train = options.n_train
    N_valid = options.n_valid
    D_in = options.n_input
    D_out = options.n_output
    epochs = options.n_epoch
    batch_size = options.n_batch
    n_sampling_combs = options.n_sampling

    X_data, X_valid, y_data, y_valid = make_dataset(N_train, N_valid, D_in)

    net = Net(D_in, D_out)
    opt = optim.Adam(net.parameters())

    for epoch in range(1, epochs+1):
        index = torch.randperm(N_train)

        X_train = X_data[index]
        y_train = y_data[index]

        for cur_batch in range(0, N_train, batch_size):
            X_batch = X_train[cur_batch: cur_batch+batch_size]
            y_batch = y_train[cur_batch: cur_batch+batch_size]

            opt.zero_grad()
            batch_loss = torch.zeros(1)
            if X_batch is not None:
                preds = net(X_batch)

                for _ in range(n_sampling_combs):
                    i, j = np.random.choice(range(preds.shape[0]), 2)
                    s_i = preds[i]
                    s_j = preds[j]

                    if y_batch[i] > y_batch[j]:
                        S_ij = 1
                    elif y_batch[i] == y_batch[j]:
                        S_ij = 0
                    else:
                        S_ij = -1
                    
                    loss = pairwise_loss(s_i, s_j, S_ij)
                    batch_loss += loss
            
            batch_loss.backward(retain_graph=True)
            opt.step()
        
        with torch.no_grad():
            valid_preds = net(X_valid)
            valid_swapped_pairs = swapped_pairs(valid_preds, y_valid)
            print(f"epoch: {epoch} valid swapped pairs: {valid_swapped_pairs}/{N_valid*(N_valid-1)//2}")

    print('DONE')


if __name__ == '__main__':
    main()
