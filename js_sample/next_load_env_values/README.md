# sample nextjs load env_values

## build in local

```shell script
yarn build
```

## run in local

```shell
yarn start
```

## build with docker

```shell script
docker-compose build
```

change parameters.

```shell script
docker-compose -f docker-compose.yml -f docker-compose.custom.yml build
```

## run with docker

```shell script
docker-compose up
```

open http://localhost:3000 on your browser.
