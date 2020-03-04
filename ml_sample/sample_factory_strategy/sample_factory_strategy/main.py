import pandas as pd
from sklearn.model_selection import train_test_split

from models.create_model import CreateModel


def main():
    df = pd.read_csv('Pokemon.csv')
    print(df.shape)

    y = df['Type 1'].values
    df.drop(['#', 'Name', 'Type 1', 'Type 2'], axis=1, inplace=True)
    X = df.values
    print(X.shape, y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
    print('## model prediction')
    for model_name in ('lda_lr', 'pca_rfc'):
        model = CreateModel().create_model(model_name)
        model.fit(X_train, y_train)
        print(f'{model_name}: ', model.score(X_test, y_test))
    
    print('DONE')


if __name__ == '__main__':
    main()
