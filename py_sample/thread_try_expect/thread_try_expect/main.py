from concurrent.futures import as_completed, ThreadPoolExecutor
import logging

import requests


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    urls = [
        'http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/'
    ]

    with ThreadPoolExecutor(max_workers=5) as executer:
        future_to_url = {
            executer.submit(requests.get, url): url for url in urls
        }

        for future in as_completed(future_to_url):
            url = future_to_url[future]

            try:
                data = future.result()
            except Exception as e:
                logger.exception(e)
            else:
                logger.info(' %r page is %d bytes', url, len(data.content))
    
    logger.info('DONE')


if __name__ == '__main__':
    main()
