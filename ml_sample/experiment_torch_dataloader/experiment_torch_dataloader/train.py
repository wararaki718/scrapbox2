import time

import torch
from torch.utils.data import DataLoader

from nn_model import NNModel


def train(dataset: 'Dataset', epochs: int=10):
    loader = DataLoader(dataset, batch_size=2, shuffle=True)

    model = NNModel(n_input=2, n_output=3)
    # model.to(device='cpu')

    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    criterion = torch.nn.CrossEntropyLoss()
 
    start_tm = time.time()
    for epoch in range(1, epochs+1):
        train_loss = 0.0
        train_acc = 0
        for x, y in loader:
            optimizer.zero_grad()

            y_pred = model(x)
            y = torch.max(torch.squeeze(y, dim=1), dim=1).indices
            
            loss = criterion(y_pred, y)
            loss.backward()
            optimizer.step()
            train_loss += loss.item()
            train_acc += (y_pred.argmax(1) == y).sum().item()
        print(f'[epoch {epoch:02d}]\tloss:{train_loss}\taccuracy:{train_acc}')
    finish_tm = time.time()
    print(f'train finished.({finish_tm-start_tm}sec)')
