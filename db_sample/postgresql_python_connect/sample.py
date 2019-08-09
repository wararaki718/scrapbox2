import sys

import psycopg2

def check_connection_status(status):
    if psycopg2.extensions.STATUS_READY == status:
        return "ready"
    
    if psycopg2.extensions.STATUS_BEGIN == status:
        return "begin"

    if psycopg2.extensions.STATUS_IN_TRANSACTION == status:
        return "transaction"
    
    if psycopg2.extensions.STATUS_PREPARED == status:
        return "prepared"
    
    return f"status none: {status}"


def main():
    # connect db
    conn = psycopg2.connect(host="localhost", user="postgres", password="password")
    print(check_connection_status(conn.status))
    conn.close()

    return 0


if __name__ == '__main__':
    sys.exit(main())
