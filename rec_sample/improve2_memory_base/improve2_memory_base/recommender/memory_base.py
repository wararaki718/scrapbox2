import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

from .base_recommender import BaseRecommender


class MemoryBaseRecommender(BaseRecommender):
    def __init__(self,
                 user_col: str='user_id',
                 item_col: str='item_id',
                 rate_col: str='rate_id'):
        self.user_col = user_col
        self.item_col = item_col
        self.rate_col = rate_col


    def fit(self, df: pd.DataFrame):
        # set values
        self.user_id2idx = {user_id: index for index, user_id in enumerate(df[self.user_col].unique())}
        self.item_id2idx = {item_id: index for index, item_id in enumerate(df[self.item_col].unique())}
        self.item_idx2id = {index: item_id for item_id, index in self.item_id2idx.items()}
        
        # cosine sims
        row = [self.user_id2idx[user_id] for user_id in df[self.user_col]]
        col = [self.item_id2idx[item_id] for item_id in df[self.item_col]]
        ratings = sparse.coo_matrix((df[self.rate_col], (row, col)))
        ratings = ratings.tocsr()
        similarities = cosine_similarity(ratings, dense_output=False)
        similarities.setdiag(0.0)
        similarities.eliminate_zeros()

        # each item's mean evaluation
        item_mean_evals = {
            item_id: df[df[self.item_col] == item_id][self.rate_col].mean()
            for item_id in self.item_id2idx.keys()
        }
        data = df[self.item_col].map(item_mean_evals)
        r_mean_items = sparse.coo_matrix((data, (row, col)))
        r_mean_items = r_mean_items.tocsr()

        # each user's mean evaluation
        user_mean_evals = np.array([
            df[df[self.user_col] == user_id][self.rate_col].mean()
            for user_id in self.user_id2idx.keys()
        ])

        # scoring
        scores = similarities.dot((ratings - r_mean_items).T) / np.array(np.abs(similarities).sum(axis=1))
        self.r = sparse.csr_matrix(user_mean_evals + scores)

        # remove evaluated items
        self.r = self.r.multiply((self.r > 0) - (ratings > 0))

        return self
        

    def recommend_k_items(self, user_id: int, top_n: int=10) -> list:
        u_index = self.user_id2idx[user_id]
        x = self.r.getrow(u_index)
        indices = np.argsort(x.data)[::-1]

        items = [{
            'item_id': self.item_idx2id[index],
            'score': x.data[index]
        } for index in indices]
        
        return items
        