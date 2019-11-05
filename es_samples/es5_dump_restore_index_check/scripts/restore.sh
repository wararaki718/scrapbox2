#!/bin/bash

REPOSITORY_NAME=my_backup_repository
SNAPSHOT_NAME=my_snapshot
INDEX_NAME=shakespeare

# delete existed index.
curl -XDELETE "localhost:9200/${INDEX_NAME}?pretty"
curl -XGET "localhost:9200/_cat/indices?v&pretty"

# restore snapshot
curl -XPOST "localhost:9200/_snapshot/${REPOSITORY_NAME}/${SNAPSHOT_NAME}/_restore?pretty"
curl -XGET "localhost:9200/_cat/indices?v&pretty"

echo "restore done."
