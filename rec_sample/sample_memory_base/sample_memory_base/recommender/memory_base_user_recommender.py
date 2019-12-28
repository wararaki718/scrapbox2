import numpy as np
from scipy import stats
from scipy import sparse

from .base_recommender import BaseRecommender


class MemoryBaseUserRecommender(BaseRecommender):
    def _get_common_indices(self, x: np.array, y: np.array) -> np.array:
        return np.intersect1d(np.where(x > 0.0)[0], np.where(y > 0.0)[0])

    def fit(self, ratings: np.array):
        (self.n_users, self.n_items) = ratings.shape

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
                    x[common_evaluated_items],
                    y[common_evaluated_items]
                )[0]

        r_means = sparse.lil_matrix((self.n_users, self.n_users))
        for i in range(self.n_users):
            x = ratings[i]
            for j in range(self.n_users):
                y = ratings[j]
                common_evaluated_items = self._get_common_indices(x, y)
                r_means[i, j] = np.mean(x[common_evaluated_items])

        self.r = sparse.lil_matrix((self.n_users, self.n_items))
        for i in range(self.n_users):
            x = ratings[i]
            not_evaluated_item_ids = np.where(x == 0.0)[0]
            for j in not_evaluated_item_ids:
                evaluated_user_ids = np.where(ratings.T[j] > 0.0)[0]
                # calc elaluated values
                p_sum = np.sum(np.absolute(p[i, evaluated_user_ids]))
                r_sum = np.sum([p[i, k] * (ratings[k, j] - r_means[k, i]) for k in evaluated_user_ids if r_means[k, i] > 0.0])
                self.r[i, j] = r_means[i, i] + r_sum / p_sum

        return self


    def recommend_k_items(self, user_id: int, top_n: int = 10) -> list:
        x = self.r[user_id]
        x_data = np.array(x.data[0])
        x_rows = np.array(x.rows[0])

        indices = np.argsort(x_data)[::-1]
        indices = indices[:top_n]

        items = [{
            'item_index': i,
            'score': score
        } for i, score in zip(x_rows[indices], x_data[indices])]
        
        return items
