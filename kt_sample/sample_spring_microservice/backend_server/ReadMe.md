# backend server

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
curl -H "Content-Type:application/json" -XPOST localhost:8080/message -d '{"content": "content", "requestTime": "2020-02-02"}'
```
