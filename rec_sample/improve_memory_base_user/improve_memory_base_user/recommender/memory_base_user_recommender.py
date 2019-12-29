import numpy as np
import pandas as pd
from scipy import stats
from scipy import sparse

from .base_recommender import BaseRecommender


class MemoryBaseUserRecommender(BaseRecommender):
    def _get_common_indices(self, x: sparse.lil_matrix, y: sparse.lil_matrix) -> np.array:
        return np.intersect1d(np.array(x.rows[0]), np.array(y.rows[0]))

    def _pearson_correlation(self, ratings: np.array) -> sparse.lil_matrix:
        p = sparse.lil_matrix((self.n_users, self.n_users))
        for i in range(self.n_users):
            x = ratings[i]
            for j in range(self.n_users):
                if i == j:
                    p[i, j] = 0
                    continue

                y = ratings[j]
                common_evaluated_items = self._get_common_indices(x, y)
                if common_evaluated_items.shape[0] < 2:
                    p[i, j] = 0
                    continue

                p[i, j] = stats.pearsonr(
                    np.array(x[0, common_evaluated_items].data[0]),
                    np.array(y[0, common_evaluated_items].data[0])
                )[0]
        return p

    def _create_adjacecy_matrix(self,
                                df: pd.DataFrame,
                                user_col: str,
                                item_col: str,
                                rate_col: str) -> sparse.lil_matrix:
        mat = sparse.lil_matrix((self.n_users, self.n_items))
        for _, row in df.iterrows():
            user_idx = self.user_id2idx[row[user_col]]
            item_idx = self.item_id2idx[row[item_col]]
            mat[user_idx, item_idx] = row[rate_col]
        return mat

    def fit(self,
            df: pd.DataFrame,
            user_col: str='user_id',
            item_col: str='item_id',
            rate_col: str='rate'):
        # set values
        self.user_id2idx = {user_id: index for index, user_id in enumerate(df[user_col].unique())}
        self.item_id2idx = {item_id: index for index, item_id in enumerate(df[item_col].unique())}
        self.item_idx2id = {index: item_id for item_id, index in self.item_id2idx.items()}
        self.n_users = len(self.user_id2idx)
        self.n_items = len(self.item_id2idx)

        ratings = self._create_adjacecy_matrix(df, user_col, item_col, rate_col)

        # calc similarities of each users
        p = self._pearson_correlation(ratings)

        # scoring
        r_means = sparse.lil_matrix((self.n_users, self.n_users))
        for i in range(self.n_users):
            x = ratings[i]
            for j in range(self.n_users):
                y = ratings[j]
                common_evaluated_items = self._get_common_indices(x, y)
                r_means[i, j] = np.mean(np.array(x[0, common_evaluated_items].data[0]))

        self.r = sparse.lil_matrix((self.n_users, self.n_items))
        item_indices = set(self.item_id2idx.values())
        ratings_transporse = ratings.transpose()

        for i in range(self.n_users):
            x = ratings[i]
            not_evaluated_item_idxs = item_indices - set(x.rows[0])
    
            for j in not_evaluated_item_idxs:
                y = ratings_transporse[j]
                evaluated_user_ids = np.array(y.rows[0])

                # calc elaluated values
                p_sum = np.sum(np.absolute(p[i, evaluated_user_ids]))
                r_sum = np.sum([p[i, k] * (ratings[k, j] - r_means[k, i]) for k in evaluated_user_ids if r_means[k, i] > 0.0])
                self.r[i, j] = r_means[i, i] + r_sum / p_sum
        return self

    def recommend_k_items(self, user_id: int, top_n: int = 10) -> list:
        x = self.r[self.user_id2idx[user_id]]
        x_data = np.array(x.data[0])
        x_rows = np.array(x.rows[0])

        indices = np.argsort(x_data)[::-1]
        indices = indices[:top_n]

        items = [{
            'item_id': self.item_idx2id[index],
            'score': score
        } for index, score in zip(x_rows[indices], x_data[indices])]
        
        return items
