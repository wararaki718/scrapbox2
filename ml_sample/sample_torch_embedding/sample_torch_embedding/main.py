import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


torch.manual_seed(42)


def main():
    word_to_ix = {"hello": 0, "world": 1}
    print(word_to_ix)
    embeds = nn.Embedding(2, 5)
    lookup_tensor =torch.tensor([word_to_ix["hello"]], dtype=torch.long)
    hello_embed = embeds(lookup_tensor)
    print(hello_embed)

if __name__ == '__main__':
    main()
