from collections import Counter

from imblearn.under_sampling import ClusterCentroids
from sklearn.datasets import make_classification


def main():
    X, y = make_classification(
        n_samples=5000,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_repeated=0,
        n_classes=3,
        n_clusters_per_class=1,
        weights=[0.01, 0.04, 0.95],
        class_sep=0.8,
        random_state=42
    )
    print(sorted(Counter(y).items()))

    cc = ClusterCentroids(random_state=42)
    X_resampled, y_resampled = cc.fit_resample(X, y)
    print(sorted(Counter(y_resampled).items()))
    print('DONE')


if __name__ == '__main__':
    main()
