# sample sqlalchemy bulk insert

## setup environment

```shell
pipenv install SQLAlchemy
```

## download sample data

```shell
bash download.sh
```

## launch mysql

```shell
docker-compose up
```

## execute a program

```shell
cd app
pipenv run python sql_movielens.py
```
