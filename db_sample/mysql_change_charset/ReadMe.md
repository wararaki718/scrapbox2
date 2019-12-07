# MySQL DB change charset

## install mysql client (for Mac)

```shell
brew install mysql
```

## start a db server

```shell
docker-compose up
```

## show charset

default setting

```shell
mysql --host 127.0.0.1 --port 3306 --user user -ppassword -e "show variables like 'character%'"
```

fixed setting

```shell
mysql --host 127.0.0.1 --port 3307 --user user -ppassword -e "show variables like 'character%'"
```
