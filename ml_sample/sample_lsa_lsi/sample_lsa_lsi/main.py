import numpy as np
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer


def main():
    texts = [
        'human machine interface for ABC computer applications',
        'a survey of user opinion of computer system response time',
        'the EPS user interface management system',
        'system and human system engineering testing of EPS',
        'relation of user perceived response time to error measurement',
        'the generation of random binary ordered trees',
        'the intersection graph of paths in trees',
        'graph minors IV widths of trees and well-quasi-ordering',
        'graph minors a survey'
    ]
    
    # create features
    vectorizer = MultiLabelBinarizer()
    features = vectorizer.fit_transform([text.split() for text in texts])

    # matrix decomposition
    U, S, Vh = np.linalg.svd(features)

    # dimensionality reduction
    n_dim = 2
    U.resize((U.shape[0], n_dim))
    S = np.diag(S[:n_dim])
    Vh.resize((n_dim, Vh.shape[1]))

    mat = U.dot(S.dot(Vh))
    
    # show the result
    print(pd.DataFrame(mat, columns=vectorizer.classes_))


if __name__ == '__main__':
    main()
