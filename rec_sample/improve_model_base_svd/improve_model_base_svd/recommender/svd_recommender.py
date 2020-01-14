import gc

import numpy as np
import pandas as pd
from scipy import sparse
from scipy.linalg import svd as scipy_svd

from .base_recommender import BaseRecommender


class SVDRecommender(BaseRecommender):
    def __init__(self,
                 user_col: str='user_id',
                 item_col: str='item_id',
                 rate_col: str='rate_id',
                 rank: int = 1000):
        self.user_col = user_col
        self.item_col = item_col
        self.rate_col = rate_col
        self.rank = rank
    
    def fit(self, df: pd.DataFrame, remove_evaluated_items: bool=True):
        # set values
        self.user_id2idx = {user_id: index for index, user_id in enumerate(df[self.user_col].unique())}
        item_id2idx = {item_id: index for index, item_id in enumerate(df[self.item_col].unique())}
        self.item_idx2id = {index: item_id for item_id, index in item_id2idx.items()}
        
        row = [self.user_id2idx[user_id] for user_id in df[self.user_col]]
        col = [item_id2idx[item_id] for item_id in df[self.item_col]]
        ratings = sparse.coo_matrix((df[self.rate_col], (row, col)))

        # fill values
        rating_df = pd.DataFrame(ratings.T.toarray())
        for index in rating_df.index:
            row = rating_df.loc[index]
            row[row == 0] = row[row > 0].mean()
            rating_df.loc[index] = row

        # calc relations
        U, s, Vh = scipy_svd(rating_df.values.T)
        del rating_df
        gc.collect()

        U.resize((U.shape[0], self.rank))
        s = sparse.diags(s[:self.rank])
        Vh.resize((self.rank, Vh.shape[1]))

        self.r = sparse.csr_matrix(U.dot(s.dot(Vh)))
        del U
        del s
        del Vh
        gc.collect()

        # remove evaluated items
        if remove_evaluated_items:
            self.r = self.r.multiply((self.r > 0) - (ratings > 0))
            self.r.eliminate_zeros()
        
        return self

    def recommend_k_items(self, user_id: int, top_n: int=10):
        u_index = self.user_id2idx[user_id]
        x = self.r.getrow(u_index)
        indices = np.argsort(x.data)[::-1]

        items = [{
            'item_id': self.item_idx2id[index],
            'score': x.data[index]
        } for index in indices[:top_n]]

        return items
