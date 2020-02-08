import pandas as pd

from recommender.svd_recommender import SVDRecommender

def main():
    df = pd.read_csv('ml-latest-small/ratings.csv')

    model = SVDRecommender(
        n_factors=10,
        n_epochs=5,
        verbose=True
    )
    model.fit(
        df=df,
        user_col='userId',
        item_col='movieId',
        rate_col='rating'
    )

    user_id = 10
    item_ids, scores = model.recommend_top_n_item(user_id)
    for item_id, score in zip(item_ids, scores):
        print(f'{item_id}: {score}')


if __name__ == "__main__":
    main()
