from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_engine(user: str,
               password: str,
               host: str,
               dbname: str,
               port:int=3306) -> Engine:
    connect_string = f'mysql+mysqldb://{user}:{password}@{host}:{port}/{dbname}'
    return create_engine(connect_string)


def main():
    user = 'user'
    password = 'password'
    host = '127.0.0.1'
    dbname = 'sample_db'
    engine = get_engine(user, password, host, dbname)

    with engine.begin() as connection:
        print(connection.info)
        print(connection.get_execution_options())
        print(connection.get_isolation_level())
        print(connection.in_transaction())
    
    print('DONE')


if __name__ == '__main__':
    main()
