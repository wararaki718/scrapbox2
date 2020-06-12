import torch
from torch.utils.data import DataLoader

from text_sentiment import TextSentiment


class ModelTrain:
    def __init__(self, vocab_size: int, num_class: int, embed_dim: int = 32):
        self._device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self._model = TextSentiment(vocab_size, embed_dim, num_class).to(self._device)
        self._criterion = torch.nn.CrossEntropyLoss().to(self._device)
        self._optimizer = torch.optim.SGD(self._model.parameters(), lr=4.0)
        self._scheduler = torch.optim.lr_scheduler.StepLR(self._optimizer, 1, gamma=0.9)

    def _generate_batch(self, batch: torch.Tensor) -> tuple:
        label = torch.tensor([entry[0] for entry in batch])
        text = [entry[1] for entry in batch]
        offsets = [0] + [len(entry) for entry in text]

        offsets = torch.tensor(offsets[:-1]).cumsum(dim=0)
        text = torch.cat(text)
        return text, offsets, label

    def train(self, sub_train_: torch.Tensor, batch_size: int=16) -> tuple:
        train_loss = 0.0
        train_acc = 0.0
        loader = DataLoader(sub_train_, batch_size, shuffle=True, collate_fn=self._generate_batch)

        for text, offsets, cls in loader:
            self._optimizer.zero_grad()
            text, offsets, cls = text.to(self._device), offsets.to(self._device), cls.to(self._device)

            output = self._model(text, offsets)
            loss = self._criterion(output, cls)
            train_loss += loss.item()
            loss.backward()
            self._optimizer.step()
            train_acc += (output.argmax(1) == cls).sum().item()
        self._scheduler.step()

        return train_loss/len(sub_train_), train_acc/len(sub_train_)

    def test(self, data_: torch.Tensor, batch_size: int=16) -> tuple:
        test_loss = 0.0
        acc = 0.0
        data = DataLoader(data_, batch_size=batch_size, collate_fn=self._generate_batch)
        for text, offsets, cls in data:
            text, offsets, cls = text.to(self._device), offsets.to(self._device), cls.to(self._device)
            with torch.no_grad():
                output = self._model(text, offsets)
                loss = self._criterion(output, cls)
                test_loss += loss.item()
                acc += (output.argmax(1) == cls).sum().item()
        
        return test_loss/len(data_), acc/len(data_)
