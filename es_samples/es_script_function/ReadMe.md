# check a behavior of a script function

## launch a elasticsearch

```shell script
docker-compose up
```

## insert data

```shell script
bash insert.sh
```

use params

```shell script
time curl -H 'Content-Type: application/json' -XGET localhost:9200/bank/account/_search?pretty -d @'queries/query.json'
```

hard-cording

```shell script
time curl -H 'Content-Type: application/json' -XGET localhost:9200/bank/account/_search?pretty -d @'queries/query.slow.json'
```
