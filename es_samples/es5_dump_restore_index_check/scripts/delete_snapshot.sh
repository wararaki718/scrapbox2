#!/bin/bash

REPOSITORY_NAME=my_backup_repository
SNAPSHOT_NAME=my_snapshot
INDEX_NAME=shakespeare

echo "delete snapshot."
curl -XGET "localhost:9200/_snapshot/${REPOSITORY_NAME}/_all?pretty"
curl -X DELETE "localhost:9200/_snapshot/${REPOSITORY_NAME}/${SNAPSHOT_NAME}?pretty"
curl -XGET "localhost:9200/_snapshot/${REPOSITORY_NAME}/_all?pretty"
echo "deleted snapshot(${SNAPSHOT_NAME})"

echo "delete repository."
curl -XGET "localhost:9200/_snapshot/_all?pretty"
curl -X DELETE "localhost:9200/_snapshot/${REPOSITORY_NAME}?pretty"
curl -XGET "localhost:9200/_snapshot/_all?pretty"
echo "deleted repository(${REPOSITORY_NAME})"

echo "delete index"
curl -XGET "localhost:9200/_cat/indices?v&pretty"
curl -XDELETE "localhost:9200/${INDEX_NAME}?pretty"
curl -XGET "localhost:9200/_cat/indices?v&pretty"
echo "delete index(${INDEX_NAME})"
