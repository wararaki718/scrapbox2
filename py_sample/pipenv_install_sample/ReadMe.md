# show pipenv packages

## build image

```shell
docker-compose build
```

## run

### prod (install default packages.)

```shell
docker-compose run prd
```

### dev (install dev and default packages.)

```shell
docker-compose run dev
```

### sys (install default packages by using system pip.)

sys does not show packages, because it doesn't use pipenv.

```shell
docker-compose run sys
```
