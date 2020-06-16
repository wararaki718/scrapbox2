import torch


def main():
    x = torch.randn(4)
    print("x:")
    print(x)
    print(x.shape)
    print()
    print("max x:")
    print(torch.max(x))
    print()

    y = torch.randn(3, 5)
    print("y:")
    print(y)
    print(y.shape)
    print()
    print("max y:")
    max_y = torch.max(y, dim=1)
    print(max_y)
    print(max_y.values)
    print(max_y.indices)
    print()

    print('DONE')


if __name__ == '__main__':
    main()
