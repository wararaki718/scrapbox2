from argparse import ArgumentParser

from elasticsearch import Elasticsearch


def get_options():
    parser = ArgumentParser()
    parser.add_argument('--es-host', dest='es_host', default='http://localhost:9200')
    parser.add_argument('--es-index', dest='es_index', default='news')
    parser.add_argument('--keyword', dest='keyword', default='チョコレート')
    return parser.parse_args()


def get_search_query(keyword: str) -> dict:
    # query = {
    #     'query': {
    #         'match_phrase': {
    #             'content': keyword
    #         }
    #     }
    # }
    query = {
        'query': {
            'match_all': {}
        }
    }
    return query


def get_mlt_query(es_index: str, document_id: str) -> dict:
    query = {
        'query': {
            'more_like_this': {
                'fields': ['title', 'content'],
                'like': [
                    {
                        '_index': es_index,
                        '_id': document_id
                    }
                ]
            }
        }
    }
    return query


def main():
    options = get_options()

    es_client = Elasticsearch(hosts=[options.es_host])
    es_query = get_search_query(options.keyword)

    response = es_client.search(index=options.es_index, body=es_query)

    hits = response.get('hits').get('hits')
    target_id = hits[0]['_id']
    print(target_id)

    es_query = get_mlt_query(options.es_index, target_id)
    response2 = es_client.search(index=options.es_index, body=es_query)

    hits = response2.get('hits').get('hits')
    print(response2)
    for hit in hits:
        print(hit['_id'])
        print(hit['title'])
        print()
    print('DONE')

if __name__ == '__main__':
    main()
