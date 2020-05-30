from datetime import date

from user import User


def main():
    u1 = User(username='taro', birthday=date(1999, 1, 1))
    u2 = User(username='jiro', birthday=date(2000, 2, 2))

    print(u1.age_display())
    print(u2.age_display())

    print('DONE')


if __name__ == '__main__':
    main()
