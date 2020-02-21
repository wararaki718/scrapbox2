#!/bin/bash

wget https://raw.githubusercontent.com/dmlc/xgboost/master/demo/data/agaricus.txt.test -P src/main/resources
wget https://raw.githubusercontent.com/dmlc/xgboost/master/demo/data/agaricus.txt.train -P src/main/resources

echo "DONE"
