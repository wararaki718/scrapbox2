#!/bin/bash

# delete existed index.
curl -XDELETE "localhost:9200/bank?pretty"
curl -XDELETE "localhost:9200/shakespeare?pretty"
curl -XGET "localhost:9200/_cat/indices?v&pretty"

# restore snapshot
curl -XPOST "localhost:9200/_snapshot/my_backup/snapshot_1/_restore?pretty"
curl -XGET "localhost:9200/_cat/indices?v&pretty"

echo "restore done."