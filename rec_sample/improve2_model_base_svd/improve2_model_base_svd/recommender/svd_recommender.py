import gc

import numpy as np
import pandas as pd
from scipy import sparse
from scipy.sparse.linalg import svds

from .base_recommender import BaseRecommender


class SVDRecommender(BaseRecommender):
    def __init__(self,
                 user_col: str='user_id',
                 item_col: str='item_id',
                 rate_col: str='rate_id',
                 rank: int=20):
        self.user_col = user_col
        self.item_col = item_col
        self.rate_col = rate_col
        self.rank = rank
    
    def fit(self, df: pd.DataFrame, remove_evaluated_items: bool=True):
        self.user_id2idx = {user_id: index for index, user_id in enumerate(df[self.user_col].unique())}
        item_id2idx = {item_id: index for index, item_id in enumerate(df[self.item_col].unique())}
        self.item_idx2id = {index: item_id for item_id, index in item_id2idx.items()}

        row = [self.user_id2idx[user_id] for user_id in df[self.user_col]]
        col = [item_id2idx[item_id] for item_id in df[self.item_col]]
        ratings = sparse.coo_matrix((df[self.rate_col], (row, col))).tocsr()
        user_rating_means = ratings.mean(axis=1)
        del row
        del col
        gc.collect()

        U, S, Vt = svds(sparse.csr_matrix(ratings - user_rating_means), k=self.rank)
        self.r = sparse.csr_matrix(U.dot(sparse.diags(S).dot(Vt)) + user_rating_means)
        del U
        del S
        del Vt
        gc.collect()

        if remove_evaluated_items:
            self.r = self.r.multiply((self.r > 0) - (ratings > 0))
            self.r.eliminate_zeros()
        
        return self


    def recommend_k_items(self, user_id: int, top_n: int=10) -> list:
        u_index = self.user_id2idx[user_id]
        x = self.r.getrow(u_index)
        indices = np.argsort(x.data)[::-1]

        items = [{
            'item_id': self.item_idx2id[index],
            'score': x.data[index]
        } for index in indices[:top_n]]

        return items
