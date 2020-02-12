# sample spring docker

## build

```shell
./gradlew jibDockerBuild --image=sample-spring:1.0
```

## run

```shell
docker-compose up
```

check

```shell
curl localhost:8080
```
