from argparse import ArgumentParser
import warnings


def parse_command_options():
    parser = ArgumentParser()
    parser.add_argument('--hidden', dest='hidden', default=False, type=bool)
    return parser.parse_args()


def main():
    options = parse_command_options()

    if options.hidden:
        warnings.simplefilter('ignore')
        print('hidden warnings.')
    
    import tensorflow
    print(f'-> {tensorflow.__version__}')
    print('done')


if __name__ == '__main__':
    main()
