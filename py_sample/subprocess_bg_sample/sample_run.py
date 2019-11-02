import subprocess


def main():
    print('start: subprocess.run')
    proc = subprocess.run(['bash', 'wait.sh'])

    print('end  : subprocess.run')
    print('main.py DONE')
    return 0


if __name__ == '__main__':
    main()
