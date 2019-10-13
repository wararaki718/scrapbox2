# sample grpc in python

## setup environment

install grpc & protocol buffer library.

```shell
pip install protobuf grpcio grpcio-tools
```

install protoc

```shell
brew install protobuf
```

## generate grpc codes

```shell
cd proto
bash generate.sh
```

after that grpc codes are generated for client and server.

## launch server

generate a docker image.

```shell
cd server
docker-compose build
```

launch grpc server

```shell
docker-compose up
```

## call server from client

```shell
cd client
python client
```
