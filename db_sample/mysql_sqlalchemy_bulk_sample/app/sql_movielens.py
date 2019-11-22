import pandas as pd
from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from base import Base
from movie import Movie


def get_engine(user: str,
               password: str,
               host: str,
               dbname: str,
               port: int=3306) -> Engine:
    connection_string = f'mysql+mysqldb://{user}:{password}@{host}:{port}/{dbname}'
    return create_engine(connection_string)


def get_tables(engine: Engine) -> list:
    inspector = inspect(engine)
    return inspector.get_table_names()


def main():
    user = 'user'
    password = 'password'
    host = '127.0.0.1'
    dbname = 'sample_db'
    engine = get_engine(user, password, host, dbname)

    # migration
    Base.metadata.create_all(bind=engine)
    print('migrated')

    # load data
    filename = 'ml-latest-small/movies.csv'
    movies = pd.read_csv(filename).head(10).rename(columns={'movieId': 'id'}).to_dict('record')
    print(movies[0])
    print('')

    # bulk insert mapping
    session = Session(bind=engine)
    session.bulk_insert_mappings(
        Movie,
        movies
    )
    session.commit()
    print('finish to insert data.')
    print('')

    # show inserted data
    print('show inserted data:')
    query = session.query(Movie).filter(Movie.id < 10)
    for movie in query.all():
        print(f'  {movie}')
    print('')
    session.close()

    # drop table
    print('drop table')
    print(f'  before: {get_tables(engine)}')
    Movie.__table__.drop(engine)
    print(f'  after : {get_tables(engine)}')
    print('')

    print('DONE')


if __name__ == '__main__':
    main()
