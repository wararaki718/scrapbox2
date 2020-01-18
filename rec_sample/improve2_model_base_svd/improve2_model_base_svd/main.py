import pandas as pd

from recommender.svd_recommender import SVDRecommender


def main():
    df = pd.read_csv('ml-latest-small/ratings.csv')
    
    model = SVDRecommender(
        user_col='userId',
        item_col='movieId',
        rate_col='rating',
        rank=100
    )
    model.fit(df)

    target_user_id = 10
    results = model.recommend_k_items(user_id=target_user_id)
    print(f'user_id: {target_user_id}')
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
