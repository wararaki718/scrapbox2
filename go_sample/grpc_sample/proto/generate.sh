#!/bin/bash

# generate grpc codes.
# python -m grpc_tools.protoc -I . --go_out=. --grpc_python_out=. sample.proto
protoc --go_out=. sample.proto
cp *.pb.go ../server/
cp *.pb.go ../client/
rm *.pb.go
