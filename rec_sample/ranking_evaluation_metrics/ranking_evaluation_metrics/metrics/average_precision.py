import pandas as pd


def average_precision(user_evaluations: pd.Series) -> float:
    ap_score = 0.0
    total_evaluation = 0
    for index, evaluation in user_evaluations.iteritems():
        if evaluation > 0:
            total_evaluation += 1
            ap_score += total_evaluation / index

    return ap_score / total_evaluation
