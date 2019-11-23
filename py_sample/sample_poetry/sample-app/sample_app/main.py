from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def main():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target
    )
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(score)


if __name__ == '__main__':
    main()
