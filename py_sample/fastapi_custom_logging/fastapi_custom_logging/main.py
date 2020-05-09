import logging

from fastapi import FastAPI
import yaml

from .module import module


logging.config.dictConfig(yaml.load(open('log_config.yml'), Loader=yaml.FullLoader))
logger = logging.getLogger('main')

app = FastAPI()


@app.get('/sample')
def sample():
    logger.critical('CRITICAL message')
    logger.error('ERROR message')
    logger.warning('WARNING message')
    logger.info('INFO message')
    logger.debug('DEBUG message')

    module()

    return 'hello, world!'
