import gc

import numpy as np
import pandas as pd
from sklearn.decomposition import NMF


def main():
    df = pd.read_csv('ml-latest-small/ratings.csv')
    table_df = df.pivot_table(index='userId', columns='movieId', values='rating')
    user_id2idx = {user_id: i for i, user_id in enumerate(table_df.index)}
    item_idx2id = {i: item_id for i, item_id in enumerate(table_df.columns)}
    print(table_df.shape)
    print(len(user_id2idx))
    print(len(item_idx2id))

    del df
    gc.collect()

    model = NMF(n_components=10)
    U = model.fit_transform(table_df.fillna(0).values)
    I = model.components_
    print(U.shape)
    print(I.shape)

    # recommend_top_n_item
    user_id = 10
    top_n = 10
    user_index = user_id2idx[user_id]
    u = U[user_index, :]
    results = u.dot(I)
    
    indices = results.argsort()[::-1]
    indices = indices[:top_n]
    item_ids = np.vectorize(lambda x: item_idx2id[x])(indices)
    for item_id, index in zip(item_ids, indices):
        print(f'{item_id}: {results[index]}')
    print('DONE')


if __name__ == '__main__':
    main()
