import numpy as np
import pandas as pd
from sklearn.decomposition import NMF


def main():
    df = pd.read_csv('ml-latest-small/ratings.csv', usecols=['userId', 'movieId', 'rating'])
    print(df.shape)

    df = pd.pivot_table(df, index='userId', columns='movieId', values='rating')
    print(df.shape)

    # NMF
    nmf_model = NMF(
        n_components=3,
        max_iter=100,
        init='random',
        random_state=42
    )
    U_nmf = nmf_model.fit_transform(df.fillna(0).values)
    I_nmf = nmf_model.components_
    print('NMF result:')
    print(U_nmf.dot(I_nmf))
    print()

    # SVD
    U_svd, S_svd, V_svd = np.linalg.svd(df.fillna(0).values)
    k = 3
    U_svd = U_svd[:, :k]
    S_svd = np.diag(S_svd[:k])
    V_svd = V_svd[:k, :]
    print('SVD result:')
    print(U_svd.dot(S_svd.dot(V_svd)))
    print()

    return 0


if __name__ == '__main__':
    main()
