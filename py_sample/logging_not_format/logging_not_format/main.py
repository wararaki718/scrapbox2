import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


def main():
    practice = 'practice'
    logger.warning(f'bad {practice}')
    logger.info(f'good %s', practice)


if __name__ == '__main__':
    main()
