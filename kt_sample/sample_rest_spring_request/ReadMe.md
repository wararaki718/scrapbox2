# sample rest-api

## build

```shell script
./gradlew build
```

## run

```shell script
./gradlew bootRun
```

## request

```shell script
curl -H "Content-Type:application/json" -XPOST localhost:8080/message -d '{"name": "name", "content": "c
ontent"}'
```
