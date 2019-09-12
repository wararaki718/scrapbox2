#!/bin/bash

## wait for statup the elasticsearch
status=''
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
wget https://download.elastic.co/demos/kibana/gettingstarted/7.x/accounts.zip
unzip accounts.zip

## load data
curl -H 'Content-Type: application/x-ndjson' -XPOST ${ES_HOST}/bank/account/_bulk?pretty --data-binary @accounts.json

## delete data
rm accounts.json accounts.zip
echo 'set data for elasticsearch'

## test
echo "do not use function_score"
curl -H 'Content-Type: application/json' -XGET ${ES_HOST}/bank/account/_search?pretty -d @'queries/query.json'

echo ""
echo "use function_score"
curl -H 'Content-Type: application/json' -XGET ${ES_HOST}/bank/account/_search?pretty -d @'queries/query.custom.json'

echo "DONE"
