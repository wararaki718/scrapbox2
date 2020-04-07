import pandas as pd


def mean_reciprocal_rank(df: pd.DataFrame) -> float:
    mrr_score = 0.0
    for colmun in df.columns:
        evaluated_df = df[df[colmun] > 0]
        if not evaluated_df.empty:
            mrr_score += 1 / evaluated_df.index[0]
    
    return mrr_score / df.shape[1]
