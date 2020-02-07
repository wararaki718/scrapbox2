import gc

import numpy as np
import pandas as pd
from scipy import sparse

from .base_recommender import BaseRecommender


class SVDRecommender(BaseRecommender):
    def __init__(self,
                 n_factors: int = 100,
                 n_epochs: int = 20,
                 biased: bool = True,
                 init_mean: int = 0,
                 init_std_dev: float = 0.1,
                 learning_rate_all: float = 0.005,
                 regularization_term_all: float = 0.02,
                 learning_rate_bu: float = None,
                 learning_rate_bi: float = None,
                 learning_rate_pu: float = None,
                 learning_rate_qi: float = None,
                 regularization_term_bu: float = None,
                 regularization_term_bi: float = None,
                 regularization_term_pu: float = None,
                 regularization_term_qi: float = None,
                 random_state: int = None,
                 verbose: bool = False):
        self.n_factors = n_factors
        self.n_epochs = n_epochs
        self.biased = biased
        self.init_mean = init_mean
        self.init_std_dev = init_std_dev
        self.learning_rate_bu = learning_rate_bu if learning_rate_bu is not None else learning_rate_all
        self.learning_rate_bi = learning_rate_bi if learning_rate_bi is not None else learning_rate_all
        self.learning_rate_pu = learning_rate_pu if learning_rate_pu is not None else learning_rate_all
        self.learning_rate_qi = learning_rate_qi if learning_rate_qi is not None else learning_rate_all
        self.regularization_term_bu = regularization_term_bu if regularization_term_bu is not None else regularization_term_all
        self.regularization_term_bi = regularization_term_bi if regularization_term_bi is not None else regularization_term_all
        self.regularization_term_pu = regularization_term_pu if regularization_term_pu is not None else regularization_term_all
        self.regularization_term_qi = regularization_term_qi if regularization_term_qi is not None else regularization_term_all
        self.random_state = random_state
        self.verbose = verbose


    def fit(self,
            df: pd.DataFrame,
            user_col: str = 'user_id',
            item_col: str = 'item_id',
            rate_col: str = 'rate_id'):
        self.user_id2idx = {user_id: index for index, user_id in enumerate(df[user_col].unique())}
        self.item_id2idx = {item_id: index for index, item_id in enumerate(df[item_col].unique())}
        self.item_idx2id = {index: item_id for item_id, index in self.item_id2idx.items()}

        if self.random_state is not None:
            np.random.seed(self.random_state)

        self._sgd(df, user_col, item_col, rate_col)


    def _sgd(self,
             df: pd.DataFrame,
             user_col: str,
             item_col: str,
             rate_col: str):
        bu = np.zeros(len(self.user_id2idx), np.double)
        bi = np.zeros(len(self.item_idx2id), np.double)
        pu = np.random.normal(
            loc=self.init_mean,
            scale=self.init_std_dev,
            size=(df[user_col].shape[0], self.n_factors)
        )
        qi = np.random.normal(
            loc=self.init_mean,
            scale=self.init_std_dev,
            size=(df[item_col].shape[0], self.n_factors)
        )

        self.global_mean = df[rate_col].mean()
        if not self.biased:
            self.global_mean = 0
        
        for epoch in range(self.n_epochs):
            if self.verbose:
                print(f'processing epoch: {epoch}')

            for _, row in df.iterrows():
                i_idx = self.item_id2idx[row[item_col]]
                u_idx = self.user_id2idx[row[user_col]]

                # compute current error
                dot = 0
                for f in range(self.n_factors):
                    dot += qi[i_idx, f] * pu[u_idx, f]
                error = row[rate_col] - (self.global_mean + bu[u_idx] + bi[i_idx] + dot)

                # update biases
                bu[u_idx] += self.learning_rate_bu * (error - self.regularization_term_bu * bu[u_idx])
                bi[i_idx] += self.learning_rate_bi * (error - self.regularization_term_bi * bi[i_idx])

                # update factors
                for f in range(self.n_factors):
                    puf = pu[u_idx, f]
                    qif = qi[i_idx, f]
                    pu[u_idx, f] += self.learning_rate_pu * (error * qif - self.regularization_term_pu * puf)
                    qi[i_idx, f] += self.learning_rate_qi * (error * puf - self.regularization_term_qi * qif)

        self.bu = bu
        self.bi = bi
        self.pu = pu
        self.qi = qi


    def estimate(self,
                 user_id: int,
                 item_id: int) -> list:
        u_idx = self.user_id2idx[user_id]
        i_idx = self.item_id2idx[item_id]

        if self.biased:
            estimates = self.global_mean
            estimates += self.bu[u_idx]
            estimates += self.bi[i_idx]
            estimates += np.dot(self.qi[i_idx], self.pu[u_idx])
        else:
            estimates = np.dot(self.qi[i_idx], self.pu[u_idx])

        return estimates
