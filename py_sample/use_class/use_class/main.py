from datetime import date

from user import User


def main():
    user = User(lastname='abc', firstname='123', birthday=date(2000, 1, 1))
    print(user.fullname)
    print(user.age)
    print('DONE')


if __name__ == '__main__':
    main()
