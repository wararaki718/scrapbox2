import logging

from modules import sub1
from modules import sub2


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('main')


def main():
    logger.info('main call')
    sub1.call_sub1()
    sub2.call_sub2()


if __name__ == '__main__':
    main()
