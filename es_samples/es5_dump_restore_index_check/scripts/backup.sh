#!/bin/bash

REPOSITORY_NAME=my_backup_repository
SNAPSHOT_NAME=my_snapshot
INDEX_NAME=shakespeare

## register a repository
curl -X PUT "localhost:9200/_snapshot/${REPOSITORY_NAME}?pretty" -H 'Content-Type: application/json' -d'
{
  "type": "fs",
  "settings": {
    "location": "/usr/share/elasticsearch/snapshots"
  }
}
'

# show info
curl -X GET "localhost:9200/_snapshot/${REPOSITORY_NAME}?pretty"

# output snapshot
curl -X PUT "localhost:9200/_snapshot/${REPOSITORY_NAME}/${SNAPSHOT_NAME}?wait_for_completion=true" -H 'Content-Type: application/json' -d'
{
  "indices": "shakespeare",
  "ignore_unavailable": true,
  "include_global_state": false
}
'

# show info
curl -X GET "localhost:9200/_snapshot/${REPOSITORY_NAME}/${SNAPSHOT_NAME}?pretty"

# delete an exsited index.
curl -XDELETE "localhost:9200/${INDEX_NAME}?pretty"
curl -XGET "localhost:9200/_cat/indices?v&pretty"

echo "backup done."
