#!/bin/bash

REPOSITORY_NAME=my_backup_repository
SNAPSHOT_NAME=my_snapshot

curl -X DELETE "localhost:9200/_snapshot/${REPOSITORY_NAME}/${SNAPSHOT_NAME}?pretty"
echo "delete snapshot."

curl -X DELETE "localhost:9200/_snapshot/${REPOSITORY_NAME}?pretty"
echo "delete repository"
