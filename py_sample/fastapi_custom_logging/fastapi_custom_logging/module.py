import logging

logger = logging.getLogger('module')

def module():
    logger.critical('CRITICAL message')
    logger.error('ERROR message')
    logger.warning('WARNING message')
    logger.info('INFO message')
    logger.debug('DEBUG message')
    