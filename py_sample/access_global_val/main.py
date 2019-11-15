from module import module as mdl

def main():
    mdl.init()
    msg = mdl.call()
    print(msg)


if __name__ == '__main__':
    main()
