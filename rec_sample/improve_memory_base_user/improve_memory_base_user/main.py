import pandas as pd

from recommender.memory_base_user_recommender import MemoryBaseUserRecommender


def main():
    df = pd.DataFrame([
        {'user_id': 1, 'item_id': 1, 'rate': 1},
        {'user_id': 1, 'item_id': 2, 'rate': 3},
        {'user_id': 1, 'item_id': 4, 'rate': 3},
        {'user_id': 2, 'item_id': 2, 'rate': 1},
        {'user_id': 2, 'item_id': 3, 'rate': 3},
        {'user_id': 3, 'item_id': 1, 'rate': 2},
        {'user_id': 3, 'item_id': 2, 'rate': 1},
        {'user_id': 3, 'item_id': 3, 'rate': 3},
        {'user_id': 3, 'item_id': 4, 'rate': 1},
        {'user_id': 4, 'item_id': 1, 'rate': 1},
        {'user_id': 4, 'item_id': 2, 'rate': 3},
        {'user_id': 4, 'item_id': 3, 'rate': 2}
    ])
    print(df)
    print(df.shape)

    model = MemoryBaseUserRecommender()
    model.fit(df)

    results = model.recommend_k_items(user_id=2)
    print(f'results: {results}')


if __name__ == '__main__':
    main()
