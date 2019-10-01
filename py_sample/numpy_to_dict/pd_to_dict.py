import sys

import pandas as pd


def main():
    df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['one', 'two'])
    print(df)

    data = df.to_dict('record')
    print(data)

    return 0


if __name__ == '__main__':
    sys.exit(main())
