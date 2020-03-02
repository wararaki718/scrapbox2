import pandas as pd
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline


def main():
    df = pd.read_csv('Pokemon.csv')
    print(df.shape)

    y = df['Type 1'].values
    df.drop(['#', 'Name', 'Type 1', 'Type 2'], axis=1, inplace=True)
    X = df.values
    print(X.shape)
    print(y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    pipeline = Pipeline([
        ('pca', PCA()),
        ('rfc', RandomForestClassifier())
    ])
    params = {
        'pca__n_components': [2, 3, 4],
        'rfc__n_estimators': [10, 20, 30],
        'rfc__max_depth': [5, 10, 15]
    }

    # grid search
    gscv = GridSearchCV(pipeline, params, cv=2)
    gscv.fit(X_train, y_train)

    # get best fit model
    model = gscv.best_estimator_
    print(model.score(X_test, y_test))


if __name__ == '__main__':
    main()
