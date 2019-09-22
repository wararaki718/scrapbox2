# sample protobuf

## setup environment (for MacOS)

```shell
brew install protobuf
```

```shell
pip install protobuf
```

## compile .proto file

```shell
protoc -I=. --python_out=. sample.proto
```

## run

```shell
python main.py
```
