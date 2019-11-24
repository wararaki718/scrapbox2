import gc
import warnings
warnings.simplefilter('ignore')

import keras
from keras.layers import Dense, Dropout
from keras.models import Sequential
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def main():
    filename = 'News_Category_Dataset_v2.json'
    df = pd.read_json(filename, orient='records', lines=True)
    print(f'load data. {df.shape}')
    print(df.columns)

    X_train, X_test, y_train, y_test = train_test_split(
        df['short_description'],
        df['category']
    )
    del df
    gc.collect()

    # tfidf vectorizer
    tfidf_vect = TfidfVectorizer()
    tfidf_vect.fit(X_train)
    n_features = len(tfidf_vect.get_feature_names())
    print(f'created vectorizer.({n_features} features)')

    # output label encoder
    label_encoder = LabelEncoder()
    label_encoder.fit(y_train)
    n_labels = len(label_encoder.classes_)
    print(f'label encoded.({n_labels} labels)')

    # output one-hot encoder
    onehot_encoder = OneHotEncoder()
    onehot_encoder.fit(y_train.to_numpy().reshape(-1, 1))
    n_categories = len(onehot_encoder.categories_)
    print(f'one-hot encoded.({n_categories} categories)')

    # nn model definition
    n_hidden = 32
    mlp_model = Sequential([
        Dense(n_hidden, activation='relu', input_dim=n_features),
        Dropout(0.5),
        Dense(n_hidden, activation='relu'),
        Dropout(0.5),
        Dense(n_hidden, activation='relu'),
        Dropout(0.5),
        Dense(n_labels, activation='softmax')
    ])
    mlp_model.compile(
        optimizer='rmsprop',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    mlp_model.fit(
        tfidf_vect.transform(X_train),
        onehot_encoder.transform(y_train.to_numpy().reshape(-1, 1)),
        epochs=5
    )
    print('mlp fit.')

    # random forest model definition
    rfc = RandomForestClassifier(
        n_estimators=32,
        n_jobs=-1,
        random_state=42
    )
    rfc.fit(
        tfidf_vect.transform(X_train),
        label_encoder.transform(y_train)
    )
    print('random forest classifier fit.')

    # model predictions and evaluations
    _, accuracy = mlp_model.evaluate(
        tfidf_vect.transform(X_test),
        onehot_encoder.transform(y_test.to_numpy().reshape(-1, 1))
    )
    print(f'mlp score: {accuracy}')

    score = rfc.score(
        tfidf_vect.transform(X_test),
        label_encoder.transform(y_test)
    )
    print(f'rfc score: {score}')

    # to implement ensemble
    # sort probas by class_
    # rfc_probas = rfc.predict_proba(tfidf_vect.transform(X_test))
    # mlp_probas = mlp_model.predict_proba(tfidf_vect.transform(X_test))


if __name__ == '__main__':
    main()
