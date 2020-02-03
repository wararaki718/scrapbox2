# use local docker-image test

## build image

```shell
docker-compose build
```

## deploy and execute k8s-cluster

```shell
kubectl apply -f ./app.yml
```

check router

```shell
curl localhost:8000/item
```

```shell
curl localhost:8000/items
```

## delete resources

```shell
kubectl delete -f ./app.yml
```
