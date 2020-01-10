import logging

from modules import sub1
from modules import sub2
from modules import sub3


logger = logging.getLogger('main')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    logger.info('main call')
    sub1.call_sub1()
    sub2.call_sub2()
    sub3.call_sub3()


if __name__ == '__main__':
    main()
