import pandas as pd

from metrics import average_precision
from metrics import mean_average_precision
from metrics import mean_reciprocal_rank


def main():
    df = pd.read_csv('data/preferred_items.csv', index_col='rank')
    print(df)
    print()

    for column in df.columns:
        print(f'AP({column}) : {average_precision(df[column])}')
    print(f'MAP: {mean_average_precision(df)}')
    print(f'MRR: {mean_reciprocal_rank(df)}')
    print()

    print('DONE')

if __name__ == '__main__':
    main()
