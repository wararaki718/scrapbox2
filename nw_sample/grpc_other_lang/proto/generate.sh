#!/bin/bash

# generate grpc codes.
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. sample.proto
protoc --go_out=plugins=grpc:. sample.proto
cp *.py ../server/
cp *.pb.go ../client/sample/

rm *.py *.pb.go
