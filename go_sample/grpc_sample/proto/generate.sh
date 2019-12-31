#!/bin/bash

# generate grpc codes.
# python -m grpc_tools.protoc -I . --go_out=. --grpc_python_out=. sample.proto
protoc --go_out=plugins=grpc:. sample.proto
cp *.pb.go ../server/sample/
cp *.pb.go ../client/sample/
rm *.pb.go
