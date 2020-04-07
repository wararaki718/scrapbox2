import pandas as pd

from .average_precision import average_precision


def mean_average_precision(df: pd.DataFrame) -> float:
    return df.apply(average_precision, axis=0).sum() / df.shape[1]
