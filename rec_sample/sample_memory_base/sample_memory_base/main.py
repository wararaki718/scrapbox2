import numpy as np
import pandas as pd
from scipy import stats
from scipy.sparse import lil_matrix


class MemoryBaseUserRecommender:
    def fit(self, x: np.array, indices: list, columns: list):
        self.id2idx = {index: i for i, index in enumerate(indices)}
        self.id2col = {column: i for i, column in enumerate(columns)}

        _x = x
        _x[np.isnan(_x)] = 0
        

        n_index = len(indices)
        p = lil_matrix((n_index, n_index))
        for i in range(n_index):
            x_i = x[i]
            for j in range(n_index):
                x_j = x[j]
                if i == j or x_i[x_i > 0].shape[0] < 2 or x_j[x_j > 0] < 2:
                    p[i][j] = 0.0
                else:
                    p[i][j] = stats.pearsonr(x_i, x_j)[0]
        
        n_column = len(columns)
        self.r = lil_matrix((n_index, n_column))
        for i in range(n_index):
            r_mean = np.mean(x[i])
            np.sum(np.absolute(p[i]))
            



    def most_similar_users(self, user_id: int, topn: int=10) -> list:
        return []
        


def main():
    rate_df = pd.read_csv('ml-latest-small/ratings.csv')
    # print(rate_df.head(5))
    table_df = pd.pivot_table(rate_df, values='rating', index='userId', columns='movieId')
    # table_df.fillna(0, inplace=True)
    print(table_df.head(5))

    user_ids = table_df.index.tolist()
    # print(user_ids)
    print(user_ids[0])
    print(table_df.iloc[user_ids[0]])

    # movie_ids = table_df.columns
    # print(movie_ids)


if __name__ == '__main__':
    main()
