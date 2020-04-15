from argparse import ArgumentParser

from elasticsearch import Elasticsearch


def get_options():
    parser = ArgumentParser()
    parser.add_argument('--es-host', dest='es_host', default='http://localhost:9200')
    parser.add_argument('--es-index', dest='es_index', default='news')
    parser.add_argument('--es-type', dest='es_type', default='doc')
    parser.add_argument('--keyword', dest='keyword', default='夏')
    return parser.parse_args()


def get_search_query(keyword: str) -> dict:
    query = {
        'query': {
            'match_phrase': {
                'content': keyword
            }
        }
    }
    return query


def get_search_all_query() -> dict:
    query = {
        'query': {
            'match_all': {}
        }
    }
    return query



def show_response(response: dict):
    hits = response.get('hits').get('hits')

    for hit in hits:
        print(hit['_id'])
        print(hit['_source']['title'])
        # print(hit)
        print()


def main():
    options = get_options()

    es_client = Elasticsearch(hosts=[options.es_host])

    print('all:')
    es_query = get_search_all_query()
    response = es_client.search(index=options.es_index, body=es_query)
    show_response(response)
    print('')

    print(f'keyword: {options.keyword}')
    es_query = get_search_query(options.keyword)
    response = es_client.search(index=options.es_index, body=es_query)
    show_response(response)

    print('DONE')


if __name__ == '__main__':
    main()
