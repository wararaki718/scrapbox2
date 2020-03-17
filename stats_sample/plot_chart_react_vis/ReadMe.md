# visualization by React

## create frontend

```shell script
yarn create next-app frontend
cd frontend
yarn add --dev react react-dom react-vis styled-components
touch next.config.js
yarn build
```

## create backend

```shell script
poetry new backend
cd backend
poetry add fastapi uvicorn pandas
```

## build docker images

```shell script
docker-compose build
```

## run

```shell script
docker-compse up
```
