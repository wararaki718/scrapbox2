#!/bin/bash

# generate grpc codes.
protoc --go_out=plugins=grpc:. sample.proto
cp *.pb.go ../server/sample/
cp *.pb.go ../client/sample/
rm *.pb.go
