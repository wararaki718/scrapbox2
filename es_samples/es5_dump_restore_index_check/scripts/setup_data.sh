#!/bin/bash

INDEX_NAME=shakespeare

## download dataset
wget https://download.elastic.co/demos/kibana/gettingstarted/shakespeare_6.0.json

## create index
curl -X PUT "localhost:9200/${INDEX_NAME}?pretty" -H 'Content-Type: application/json' -d'
{
 "mappings": {
  "doc": {
   "properties": {
    "speaker": {"type": "keyword"},
    "play_name": {"type": "keyword"},
    "line_id": {"type": "integer"},
    "speech_number": {"type": "integer"}
   }
  }
 }
}
'

## load the dataset
curl -H 'Content-Type: application/x-ndjson' -XPOST "localhost:9200/${INDEX_NAME}/doc/_bulk?pretty" --data-binary @shakespeare_6.0.json

## delete the dataset
rm shakespeare_6.0.json

echo "setup done"
