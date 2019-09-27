import inspect
import sys


def sample_func():
    print('hello, world')

def main():
    func = sample_func
    
    print('show function address')
    print(func)
    print('')
    print('show function source')
    print(inspect.getsource(func))

    return 0


if __name__ == '__main__':
    sys.exit(main())
