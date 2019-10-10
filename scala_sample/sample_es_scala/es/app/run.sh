#!/bin/bash

## wait for statup the elasticsearch
status='red'
while [ "$status" != "green" ]
do
    echo "elasticsearch status: $status"
    sleep 10
    response=`curl ${ES_HOST}/_cat/health?h=status`
    status=`echo "$response" | sed -r 's/^[[:space:]]+|[[:space:]]+$//g'`
done
echo "elasticsearch status: $status"


## set accounts
## download
wget https://download.elastic.co/demos/kibana/gettingstarted/accounts.zip
unzip accounts.zip

## load data
curl -H 'Content-Type: application/x-ndjson' -XPOST ${ES_HOST}/bank/account/_bulk?pretty --data-binary @accounts.json

## delete data
rm accounts.json accounts.zip
echo 'set data for elasticsearch'
