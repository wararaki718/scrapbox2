# build & runs

## to build & start up elasticsearch

```
docker-compose up
```

## setup dataset

```shell
cd scripts
sh setup_data.sh
```

check inserted data

```shell
curl -XGET localhost:9200/shakespeare/_search"?pretty"
```

## create snapshot

```shell
sh backup.sh
```

## restore index

```shell
sh restore.sh
```

check restored data

```shell
curl -XGET localhost:9200/shakespeare/_search"?pretty"
```

## delete snapshot

```shell
sh delete_all.sh
```
