from argparse import ArgumentParser

from elasticsearch import Elasticsearch, helpers

from news_iterator import NewsIterator


def get_options():
    parser = ArgumentParser()
    parser.add_argument('--es-host', dest='es_host', default='http://localhost:9200')
    parser.add_argument('--es-index', dest='es_index', default='news')
    return parser.parse_args()


def get_mapping() -> dict:
    es_mapping = {
        'mappings': {
            'properties': {
                'url': {'type': 'text'},
                'datetime': {'type': 'text'},
                'title': {
                    'type': 'text',
                    'fielddata': True,
                    'analyzer': 'kuromoji_analyzer',
                    'term_vector': 'yes'
                },
                'content': {
                    'type': 'text',
                    'fielddata': True,
                    'analyzer': 'kuromoji_analyzer',
                    'term_vector': 'yes'
                },
                'label': {'type': 'keyword'}
            }
        },
        'settings': {
            'analysis': {
                'analyzer': {
                    'kuromoji_analyzer': {
                        'type': 'custom',
                        'tokenizer': 'kuromoji_tokenizer'
                    }
                }
            }
        }
    }
    return es_mapping


def main():
    options = get_options()
    es_host = options.es_host
    es_index = options.es_index

    es_client = Elasticsearch(hosts=[es_host])

    # set index
    es_mapping = get_mapping()
    es_client.indices.create(index=es_index, body=es_mapping)

    def load_news(dir_path:str, es_index: str):
        news_iter = NewsIterator(dir_path)
        for news in news_iter:
            yield {
                '_index': es_index,
                'doc': news.to_dict()
            }

    # bulk insert
    dir_path = 'text/*/*.txt'
    helpers.bulk(es_client, load_news(dir_path, es_index))
    
    print('setup done.')
    

if __name__ == '__main__':
    main()
