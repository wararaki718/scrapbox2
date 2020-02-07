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
    movie_id = 10

    print(model.estimate(user_id, movie_id))


if __name__ == "__main__":
    main()
