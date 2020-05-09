# sample custom logging fastapi

## install packages

```shell script
poetry install
```

## run

```shell script
poetry run uvicorn fastapi_custom_logging.main:app
```

call api

```shell script
curl -XGET localhost:8000/sample
```
