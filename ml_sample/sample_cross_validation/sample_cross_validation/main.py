from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.tree import DecisionTreeClassifier


def main():
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, shuffle=True, random_state=42)
    dtc = DecisionTreeClassifier()
    
    cv_results = cross_validate(dtc, X_train, y_train, cv=5, return_estimator=True, n_jobs=-1)
    estimators = cv_results.get('estimator')
    test_results = []
    for estimator in estimators:
        print('model info: ', end='')
        print(estimator.get_params())
        test_results.append(estimator.score(X_test, y_test))
    print()
    print('cv_test score  : ', end='')
    print(list(cv_results.get('test_score')))
    print('test data score: ', end='')
    print(test_results)
    print('DONE')


if __name__ == '__main__':
    main()
