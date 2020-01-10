import logging


logger = logging.getLogger('main').getChild(__name__)


def call_sub2():
    logger.info('sub2 call')
