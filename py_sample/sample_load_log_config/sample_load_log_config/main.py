import logging
import logging.config

import yaml

from module import module


logging.config.dictConfig(yaml.load(open('log_config.yml'), Loader=yaml.FullLoader))
logger = logging.getLogger('main')


def main():
    logger.critical('CRITICAL message')
    logger.error('ERROR message')
    logger.warning('WARNING message')
    logger.info('INFO message')
    logger.debug('DEBUG message')

    module()


if __name__ == '__main__':
    main()
