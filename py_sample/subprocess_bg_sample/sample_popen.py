import subprocess


def main():
    print('start: subprocess.Popen')
    proc = subprocess.Popen(['bash', 'wait.sh'])

    print('end  : subprocess.Popen')
    print('main.py DONE')
    return 0


if __name__ == '__main__':
    main()
