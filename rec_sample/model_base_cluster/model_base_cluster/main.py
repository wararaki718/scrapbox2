import gc

import pandas as pd
from scipy import sparse
from sklearn.cluster import KMeans


def get_feature_df(merge_df: pd.DataFrame) -> pd.DataFrame:
    features = []
    user_ids = merge_df.userId.unique()
    for user_id in user_ids:
        user_df = merge_df[merge_df.userId == user_id]
        genres = set()
        for movie_genres in user_df.genres:
            genres |= set(movie_genres.split('|'))
        feature = {'userId': user_id}
        for genre in genres:
            genre_df = user_df[user_df.genres.str.contains(genre)]
            feature[f'{genre}_mean_rating'] = genre_df.rating.mean()
        features.append(feature)
    
    return pd.DataFrame(features).sort_values('userId').reset_index()


def get_predict_df(feature_df: pd.DataFrame) -> pd.DataFrame:
    model = KMeans(n_clusters=10)
    predicts = model.fit_predict(
        feature_df.drop(labels=['userId'], axis=1).fillna(0.0).values
    )

    pred_df = pd.DataFrame({
        'userId': feature_df.userId,
        'clusterLabel': predicts
    })
    
    return pred_df


def get_recommendations(cluster_label: int, cluster_df: pd.DataFrame, top_n: int=10) -> list:
    target_df = cluster_df[cluster_df.clusterLabel == cluster_label]
    mean_rates = target_df.groupby(['movieId'])['rating'].mean()
    mean_rates.sort_values(ascending=False, inplace=True)
    
    results = [{
        'movieId': index,
        'score': value
    } for index, value in mean_rates.iteritems()]

    return results[:top_n]


def main():
    rate_df = pd.read_csv('ml-latest-small/ratings.csv')
    movie_df = pd.read_csv('ml-latest-small/movies.csv')
    print(rate_df.shape)
    print(movie_df.shape)

    merge_df = pd.merge(rate_df, movie_df, on='movieId')
    print(merge_df.shape)
    del rate_df
    del movie_df
    gc.collect()

    # preprocessing
    feature_df = get_feature_df(merge_df)
    print(feature_df.shape)

    # clustering
    pred_df = get_predict_df(feature_df)
    print(pred_df.shape)
    del feature_df
    gc.collect()
    
    # recommendation
    cluster_df = pd.merge(merge_df, pred_df, on='userId')
    print(cluster_df.shape)
    del merge_df
    del pred_df
    gc.collect()

    cluster_label = 1
    results = get_recommendations(cluster_label, cluster_df)
    print(f'target cluster label: {cluster_label}')
    for result in results:
        print(f'movieId: {result["movieId"]}, score: {result["score"]}')


if __name__ == '__main__':
    main()
