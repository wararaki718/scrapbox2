from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.pipeline import Pipeline


def main():
    news = fetch_20newsgroups()
    X = news.data
    y = news.target

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    print(len(X), len(y))
    print(len(X_train), len(y_train))
    print(len(X_test), len(y_test))

    # model definition
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('nb', BernoulliNB())
    ])

    # model train
    pipeline.fit(X_train, y_train)

    # model prediction
    print(pipeline.score(X_test, y_test))


if __name__ == '__main__':
    main()
