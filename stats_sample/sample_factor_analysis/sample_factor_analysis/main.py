import pandas as pd
from sklearn.decomposition import FactorAnalysis


def main():
    df = pd.read_csv('data/Pokemon.csv')
    X = df[
        ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']
    ].values

    fa = FactorAnalysis(n_components=2, tol=0.001, random_state=42)
    X_new = fa.fit_transform(X)

    print('X_new')
    print(X_new.shape)
    print(X_new)
    print('')

    print('components')
    print(fa.components_.shape)
    print(fa.components_)


if __name__ == '__main__':
    main()
