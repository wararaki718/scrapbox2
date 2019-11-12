import logging

import mysql.connector
import pandas as pd


def init_logger() -> logging.Logger:
    logging.basicConfig(
        format='%(asctime)s-%(levelname)s: %(message)s',
        level=logging.INFO
    )
    return logging.getLogger(__name__)


def get_db_connection(user_name: str='user',
                      password: str='password',
                      host: str='127.0.0.1',
                      db_name: str='sample_db') -> mysql.connector.MySQLConnection:
    connection = mysql.connector.connect(
        user=user_name,
        password=password,
        host=host,
        database=db_name
    )
    return connection


def create_table(connection: mysql.connector.MySQLConnection,
                 table_name: str):
    cursor = connection.cursor()
    query = f"""
    CREATE TABLE {table_name} (
        id int,
        name varchar(64),
        PRIMARY KEY (id)
    )
    """
    cursor.execute(query)
    cursor.close()


def delete_table(connection: mysql.connector.MySQLConnection,
                 table_name: str):
    cursor = connection.cursor()
    query = f"""
        DROP TABLE {table_name}
    """
    cursor.execute(query)
    cursor.close()


def insert_data(connection: mysql.connector.MySQLConnection,
                table_name: str,
                data: dict):
    cursor = connection.cursor()
    query = f"""
        INSERT INTO {table_name} (id, name) VALUES (%(id)s, %(name)s)
    """
    cursor.execute(query, data)
    
    # commit
    connection.commit()
    cursor.close()


def insert_bulk_data(connection: mysql.connector.MySQLConnection,
                     table_name: str,
                     data: list):
    cursor = connection.cursor()
    query = f"""
        INSERT INTO {table_name} (id, name) VALUES (%(id)s, %(name)s)
    """
    cursor.executemany(query, data)
    
    # commit
    connection.commit()
    cursor.close()


def show_data(connection: mysql.connector.MySQLConnection,
              table_name: str):
    cursor = connection.cursor()
    query = f"""
        SELECT * FROM {table_name}
    """
    cursor.execute(query)
    for row in cursor:
        print(row)
    cursor.close()


def show_tables(connection: mysql.connector.MySQLConnection):
    cursor = connection.cursor()
    query = f"""
        show tables
    """
    cursor.execute(query)
    print(cursor.fetchone())
    cursor.close()


def main():
    logger = init_logger()
    df = pd.read_csv('data/Pokemon.csv').rename(columns={'#': 'Id'}).drop_duplicates('Id')
    logger.info(df.shape)
    logger.info(df.columns)

    connection = get_db_connection()
    logger.info(f'DB connection :{connection.is_connected()}')
    table_name = 'pokemon'
    show_tables(connection)

    logger.info('create table.')
    create_table(connection, table_name)
    show_tables(connection)

    logger.info('insert data')
    insert_data(connection, table_name, {'id': 0, 'name': 'test'})

    logger.info('bulk insert')
    data = []
    for row in df.head(20).itertuples():
        data.append({'id': row.Id, 'name': row.Name})
    insert_bulk_data(connection, table_name, data)
    show_data(connection, table_name)

    logger.info('delete table.')
    delete_table(connection, table_name)
    show_tables(connection)

    connection.close()


if __name__ == '__main__':
    main()
