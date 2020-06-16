import torch


def main():
    loss = torch.nn.CrossEntropyLoss()

    x = torch.randn(3, 5, requires_grad=True)
    print('x: ')
    print(x)
    print(x.shape)
    print()

    target = torch.empty(3, dtype=torch.long).random_(5)
    print('target: ')
    print(target)
    print(target.shape)
    print()

    output = loss(x, target)
    print('loss: ')
    print(output)
    print()

    output.backward()

    print('DONE')


if __name__ == '__main__':
    main()
