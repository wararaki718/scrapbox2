from argparse import ArgumentParser

from elasticsearch import Elasticsearch
from sklearn.preprocessing import OneHotEncoder


def get_options():
    parser = ArgumentParser()
    parser.add_argument('--es-host', dest='es_host', default='http://localhost:9200')
    parser.add_argument('--es-index', dest='es_index', default='news')
    parser.add_argument('--es-type', dest='es_type', default='doc')
    parser.add_argument('--keyword', dest='keyword', default='夏')
    parser.add_argument('--label', dest='label', default='smax')
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


def get_search_similarity_query(keyword: str, query_vector: list) -> dict:
    query = {
        'query': {
            'script_score': {
                'query': {
                    'match_phrase': {
                        'content': keyword
                    }
                },
                'script': {
                    'source': "cosineSimilarity(params.query_vector, doc['content_vector']) + 1.0",
                    'params': {'query_vector': query_vector}
                }
            }
        }
    }
    return query


def show_response(response: dict):
    hits = response.get('hits').get('hits')

    for i, hit in enumerate(hits):
        print(i, hit['_source']['label'], hit['_source']['title'])

def get_encoder():
    labels = [
        ['dokujo-tsushin'],
        ['it-life-hack'],
        ['kaden-channel'],
        ['livedoor-homme'],
        ['movie-enter'],
        ['peachy'],
        ['smax'],
        ['sports-watch'],
        ['topic-news']
    ]
    encoder = OneHotEncoder().fit(labels)
    return encoder


def main():
    options = get_options()

    es_client = Elasticsearch(hosts=[options.es_host])
    encoder = get_encoder()

    print('all:')
    es_query = get_search_all_query()
    response = es_client.search(index=options.es_index, body=es_query)
    show_response(response)
    print()

    print(f'keyword: {options.keyword}')
    es_query = get_search_query(options.keyword)
    response = es_client.search(index=options.es_index, body=es_query)
    show_response(response)
    print()

    print(f'cosine_similarity: {options.keyword}, {options.label}')
    query_vector = encoder.transform([[options.label]]).toarray()[0].tolist()
    es_query = get_search_similarity_query(options.keyword, query_vector)
    response = es_client.search(index=options.es_index, body=es_query)
    show_response(response)

    print('DONE')


if __name__ == '__main__':
    main()
