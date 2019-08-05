#!/bin/bash

status=1
while [ $status != 0 ]
do
    sleep 10
    mysql --host $HOST --port $PORT --user $USER -p$PASSWORD -e "show databases;" > /dev/null 2>&1
    status=$?
    echo "mysql status: $status"
done

echo "connected mysql!"
echo "DONE!"
