import logging

from module import load_sales_csv, store_total_sales

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


def main():
    try:
        logger.info('売上CSV取り込み処理開始')

        sales_data = load_sales_csv()
        logger.info('売上CSV読み込み済み')

        for code, sales_rows in sales_data:
            logger.info('取り込み開始 - 店舗コード: %s, データ件数: %s', code, len(sales_data))
            try:
                for i, row in enumerate(sales_rows, start=1):
                    logger.debug('取り込み処理中 - 店舗(%s): %s行目', code, i)
                    store_total_sales(code, row)
            except Exception as exc:
                logger.warning('取り込みエラー = 店舗(%s) %s行目: エラー %s', code, i, exc, exc_info=True)
                continue
            logger.info('取り込み正常終了 - 店舗コード: %s', code)
        logger.info('売上csv取り込み処理終了')
    except Exception as exc:
        logger.error('売上csv取り込み処理で予期しないエラー発生: エラー %s', exc, exc_info=True)


if __name__ == '__main__':
    main()
