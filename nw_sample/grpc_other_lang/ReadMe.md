# sample grpc other languages

## setup protobuf (install protoc)

```shell
brew install protobuf
```

## setup environment

```shell
go get -u github.com/golang/protobuf/protoc-gen-go
```

## generate codes

```shell
cd proto
bash generate.sh
```

## build

client

```shell
cd client
go build -o client main.go
```

server

```shell
cd server
docker-compose build
```

## run

server

```shell
cd server
docker-compose up
```

client

```shell
cd client
./client
```
