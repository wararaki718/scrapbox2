import json
import os
import sys

from elasticsearch import Elasticsearch


def create_es_query() -> dict:
    query = {
        'query': {
            'match_all': {}
        },
        'size': 10
    }
    return query


def main():
    es_host = os.getenv('ES_HOST')
    es_index = os.getenv('ES_INDEX')
    es_query = create_es_query()

    es = Elasticsearch(hosts=[es_host])
    response = es.search(
        index=es_index,
        body=es_query,
        request_timeout=1000,
        scroll='2m'
    )

    print('scroll start!')
    scroll_id = response.get('_scroll_id')
    data = response.get('hits').get('hits')
    max_size = 100
    while max_size > len(data):
        response = es.scroll(
            scroll_id=scroll_id,
            scroll='2m'
        )
        data.extend(response.get('hits').get('hits'))

        ## show info
        print(f'size of data: {len(data)}')
        print(json.dumps(data[-1]))
    print('finish scroll!')

    return 0


if __name__ == '__main__':
    sys.exit(main())
