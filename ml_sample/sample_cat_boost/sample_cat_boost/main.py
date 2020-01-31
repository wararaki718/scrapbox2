from catboost import CatBoostClassifier
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
    

def main():
    df = pd.read_csv('Pokemon.csv').dropna()
    y = df['Type 1']
    X = df.drop(['#', 'Name', 'Type 1',], axis=1)
    categorical_features_indices = np.where(X.dtypes != np.float)[0]
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = CatBoostClassifier(
        custom_loss=['Accuracy'],
        random_seed=42,
        logging_level='Verbose'
    )
    model.fit(
        X_train,
        y_train,
        cat_features=categorical_features_indices,
        eval_set=(X_test, y_test)
    )
    y_preds = model.predict(X_test)
    print(f'accuracy: {accuracy_score(y_test, y_preds)}')

    return 0


if __name__ == '__main__':
    main()
