from typing import List, Tuple

def load_sales_csv() -> List[Tuple]:
    return [
        (1, [100, 200, 300]),
        (2, [400, 500, 600])
    ]

def store_total_sales(code: int, total: int):
    dummy_session = (code, total)
