# sample fastapi logger

## install packages

```shell script
poetry install
```

## run

```shell script
poetry run uvicorn fastapi_logger.main:app
```

check

```shell script
curl -XGET localhost:8000/sample
```
