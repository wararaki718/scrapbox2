from xmlrpc.client import ServerProxy


def main():
    with ServerProxy('http://localhost:8000') as proxy:
        print(f'pow: {proxy.pow(2, 3)}')
        print(f'add: {proxy.add(2, 3)}')
        print(f'mul: {proxy.mul(2, 3)}')
        print(proxy.system.listMethods())
    print('DONE')

    return 0


if __name__ == '__main__':
    main()
