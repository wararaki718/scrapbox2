#!/bin/bash

DATA_DIR=app/data
mkdir -p $DATA_DIR

## download data
wget https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.train -P $DATA_DIR
wget https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.train.query -P $DATA_DIR
wget https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.test -P $DATA_DIR
wget https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.test.query -P $DATA_DIR

echo "download complete"
