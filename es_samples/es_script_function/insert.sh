#!/bin/bash

ES_HOST=localhost:9200

## set accounts
## download
wget https://download.elastic.co/demos/kibana/gettingstarted/7.x/accounts.zip
unzip accounts.zip

## load data
curl -H 'Content-Type: application/x-ndjson' -XPOST ${ES_HOST}/bank/account/_bulk?pretty --data-binary @accounts.json

## delete data
rm accounts.json accounts.zip
echo 'set data for elasticsearch'

echo "DONE"
