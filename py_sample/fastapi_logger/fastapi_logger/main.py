from fastapi import FastAPI
from fastapi.logger import logger

from .module import module

app = FastAPI()


@app.get('/sample')
def sample():
    logger.critical('CRITICAL message')
    logger.error('ERROR message')
    logger.warning('WARNING message')
    logger.info('INFO message')
    logger.debug('DEBUG message')

    module()
    
    return 'hello, world'
