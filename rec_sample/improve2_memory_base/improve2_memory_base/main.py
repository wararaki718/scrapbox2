import pandas as pd

from recommender.memory_base import MemoryBaseRecommender


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

    model = MemoryBaseRecommender(user_col='user_id', item_col='item_id', rate_col='rate')
    model.fit(df)

    target_id = 2
    results = model.recommend_k_items(user_id=target_id)
    print(f'user_id: {target_id}, results: {results}')


if __name__ == '__main__':
    main()
