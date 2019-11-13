# sample pipenv application

this is an api server based on fastapi.
This project is created by using Pipenv.

## run local

```shell
bash docker-entrypoint.sh
```

```shell
pipenv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## using a docker container

### build

```shell
docker-compose build
```

### run

```shell
docker-compose up
```

if you check a connection of the server, you visit http://localhost:8000/hello on your browser or execute a below command on your terminal.

```shell
curl -X GET localhost:8000/hello
```
