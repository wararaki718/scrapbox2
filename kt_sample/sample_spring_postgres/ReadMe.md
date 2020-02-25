# sample

## launch postgres

```shell
docker-compose up
```

## create database

login

```shell
psql -h 127.0.0.1 -p 5432 -U postgres
```

create database

```shell
postgres# CREATE DATABASE testdb;
```

show dbs

```shell
postgres# \l
```

```shell
postgres# exit
```

## db operations

insert data

```shell
curl http://localhost:8080/save
```

show all

```shell
curl http://localhost:8080/findall
```

find by id

```shell
curl http://localhost:8080/findbyid/1
```

find by lastname

```shell
curl http://localhost:8080/findbylastname/Mame
```
