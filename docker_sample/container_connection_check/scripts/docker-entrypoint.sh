# set accounts

status='red'
while [ "$status" != "green" ]
do
    echo "elasticsearch status: $status"
    sleep 10
    response=`curl ${ES_HOST}:${ES_PORT}/_cat/health?h=status`
    status=`echo "$response" | sed -r 's/^[[:space:]]+|[[:space:]]+$//g'`
done

## download
wget https://download.elastic.co/demos/kibana/gettingstarted/accounts.zip
unzip accounts.zip

## load data
curl -H 'Content-Type: application/x-ndjson' -X POST "${ES_HOST}:${ES_PORT}/bank/account/_bulk?pretty" --data-binary @accounts.json

## escape status yellow
curl -H 'Content-Type: application/json' -X PUT "${ES_HOST}:${ES_PORT}/bank/_settings?pretty" -d '{"number_of_replicas": 0}'

## check status
curl -XGET "${ES_HOST}:${ES_PORT}/_cat/indices?v&pretty"

## delete data
rm accounts.json accounts.zip

echo "setup done"