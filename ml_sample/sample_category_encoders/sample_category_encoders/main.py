import category_encoders as ce
import pandas as pd


def main():
    category_cols = ['Type 1']
    df = pd.read_csv('Pokemon.csv', usecols=category_cols)
    print(df)

    # one-hot
    encoder = ce.OneHotEncoder(cols=category_cols)
    encoded_df = encoder.fit_transform(df)
    print(encoded_df)

    # ordinal
    encoder = ce.OrdinalEncoder(cols=category_cols)
    encoded_df = encoder.fit_transform(df)
    print(encoded_df)

    return 0


if __name__ == '__main__':
    main()
