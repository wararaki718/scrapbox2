#!/bin/bash

# generate grpc codes.
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. sample.proto
cp *.py ../server/
cp *.py ../client/
rm *.py
