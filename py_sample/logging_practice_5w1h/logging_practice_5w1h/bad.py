import logging

from module import load_sales_csv, store_total_sales

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


def main():
    logger.info('取り込み開始')

    sales_data = load_sales_csv()

    for code, sales_rows in sales_data:
        logger.info('取り込み中')
        try:
            for row in sales_rows:
                store_total_sales(code, row)
        except:
            logger.error('エラー発生')
    logger.info('取り込み処理終了')


if __name__ == '__main__':
    main()
