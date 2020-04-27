from glob import glob
import logging

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from tqdm import tqdm

from news_interator import NewsIterator
from nn_classifier import NNClassifier
from text_tokenizer import TextTokenizer

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


def main():
    dir_path = 'text/*/*.txt'
    n_news = len(glob(dir_path))

    logger.info('load data')
    news_iter = NewsIterator(dir_path)
    X = []
    y = []
    tokenizer = TextTokenizer()
    with tqdm(total=n_news) as pbar:
        for news in news_iter:
            X.append(tokenizer(news.content))
            y.append(news.label)
            pbar.update(1)
    logger.info(f'loaded ({len(y)})')
    
    X = np.array(X)
    y = np.array(y)
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('nn', NNClassifier())
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    
    logger.info('train start:')
    pipeline.fit(X_train, y_train)

    logger.info('test start')
    y_preds = pipeline.predict(X_test)
    score = accuracy_score(y_test, y_preds)
    print(f'score: {score}')
    print('DONE')


if __name__ == '__main__':
    main()
