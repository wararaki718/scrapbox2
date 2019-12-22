import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


torch.manual_seed(42)


def create_dataset(text: str) -> list:
    data = []
    for i in range(2, len(text)-2):
        context = [
            text[i-2],
            text[i-1],
            text[i+1],
            text[i+2]
        ]
        target = text[i]
        data.append((context, target))
    return data


class CBOW(nn.Module):
    def __init__(self,
                 context_size: int=2,
                 embedding_size: int=100,
                 hidden_size: int=100,
                 vocab_size: int=None):
        super(CBOW, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_size)
        self.linear1 = nn.Linear(2 * context_size * embedding_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, vocab_size)

    def forward(self, inputs: list):
        embedded = self.embeddings(inputs).view((1, -1))
        hidden = F.relu(self.linear1(embedded))
        outputs = self.linear2(hidden)
        return F.log_softmax(outputs)


def main():
    CONTEXT_SIZE = 2  # 2 words to the left, 2 to the right
    EMBEDDING_SIZE = 10
    raw_text = """We are about to study the idea of a computational process.
    Computational processes are abstract beings that inhabit computers.
    As they evolve, processes manipulate other abstract things called data.
    The evolution of a process is directed by a pattern of rules
    called a program. People create programs to direct processes. In effect,
    we conjure the spirits of the computer with our spells.""".split()

    vocab = set(raw_text)
    vocab_size = len(vocab)

    word_to_ix = {word: i for i, word in enumerate(vocab)}
    ix_to_word = {i: word for i, word in enumerate(vocab)}

    # model train
    loss_func = nn.CrossEntropyLoss()
    model = CBOW(CONTEXT_SIZE, embedding_size=EMBEDDING_SIZE, vocab_size=vocab_size)
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    data = create_dataset(raw_text)

    n_epoch = 100
    for epoch in range(n_epoch):
        total_loss = 0.0
        for context, target in data:
            indices = [word_to_ix[word] for word in context]
            context_var = Variable(torch.tensor(indices, dtype=torch.long))

            model.zero_grad()
            log_probs = model(context_var)

            loss = loss_func(
                log_probs,
                Variable(torch.tensor([word_to_ix[target]], dtype=torch.long))
            )

            loss.backward()
            optimizer.step()

            total_loss += loss.data
        print(epoch, total_loss)
    
    # model test
    for context, target in data:
        context_indices = [word_to_ix[word] for word in context]
        context_var = Variable(torch.tensor(context_indices, dtype=torch.long))

        model.zero_grad()
        log_probs = model(context_var)

        _, predicted = torch.max(log_probs.data, 1)
        predicted_word = ix_to_word[predicted.item()]
        print(f'predict: {predicted_word}')
        print(f'label  : {target}')
    

if __name__ == '__main__':
    main()
