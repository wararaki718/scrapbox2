# MySQL DB connection

## setup environment

set environment variables, because these variables are needed to install mysqlclient.

```shell
brew install openssl
```


```shell
export PATH="/usr/local/opt/openssl/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
```

## install packages

use pip in system

```shell
pip install mysqlclient SQLAlchemy
```

use pipenv

```shell
pipenv install mysqlclient SQLAlchemy
```

## start a db server

```shell
docker-compose up
```

## execute a sample program

```shell
pipenv run python sample_connection.py
```
