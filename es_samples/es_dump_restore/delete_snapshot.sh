#!/bin/bash

curl -X DELETE "localhost:9200/_snapshot/my_backup/snapshot_1?pretty"
echo "delete snapshot."

curl -X DELETE "localhost:9200/_snapshot/my_backup?pretty"
echo "delete repository"
