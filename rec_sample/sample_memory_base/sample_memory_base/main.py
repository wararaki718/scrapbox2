import pandas as pd

from recommender.memory_base_user_recommender import MemoryBaseUserRecommender


def main():
    df = pd.DataFrame([[1, 3, 0, 3], [0, 1, 3, 0], [2, 1, 3, 1], [1, 3, 2, 0]])
    print(df)

    model = MemoryBaseUserRecommender()
    model.fit(df.values)

    results = model.recommend_k_items(user_id=1)
    print(results)


if __name__ == '__main__':
    main()
