import sys

import psycopg2


def main():
    # connect db
    conn = psycopg2.connect(host="localhost", user="postgres", password="password")
    print(conn.status)
    conn.close()

    return 0


if __name__ == '__main__':
    sys.exit(main())
