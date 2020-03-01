import pandas as pd
from sklearn.decomposition import PCA


def main():
    df = pd.read_csv('data/Pokemon.csv')
    df = df[['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']]
    
    pca = PCA(n_components=2)
    features = pca.fit_transform(df.values)
    print(df.shape)
    print(features.shape)
    print(features)
    print('DONE')


if __name__ == '__main__':
    main()
