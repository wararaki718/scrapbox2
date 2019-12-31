# sample grpc

## setup protobuf (intall protoc)

```shell
brew install protobuf
```

## generate grpc codes

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
go build -o server main.go
```

## run

server

```shell
cd server
./server
```

client

```shell
cd client
./client
```
