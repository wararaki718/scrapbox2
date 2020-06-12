import logging
import os
import time

from torch.utils.data.dataset import random_split
import torchtext
from torchtext.datasets import text_classification

from model_train import ModelTrain


NGRAMS = 2
N_EPOCHS = 5

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info('start')
    download_data_path = './.data'
    if not os.path.isdir(download_data_path):
        os.mkdir(download_data_path)
        logger.info('%s is created', download_data_path)

    train_dataset, test_dataset = text_classification.DATASETS['AG_NEWS'](root=download_data_path, ngrams=NGRAMS, vocab=None)
    logger.info('data loaded')

    vocab_size = len(train_dataset.get_vocab())
    num_class = len(train_dataset.get_labels())
    model_train = ModelTrain(vocab_size, num_class)
    logger.info('model defined')

    min_valid_loss = float('inf')
    n_train = int(len(train_dataset) * 0.95)
    sub_train_, sub_valid_ = random_split(train_dataset, [n_train, len(train_dataset)-n_train])

    for epoch in range(N_EPOCHS):
        start_tm = time.time()
        train_loss, train_acc = model_train.train(sub_train_)
        valid_loss, valid_acc = model_train.test(sub_valid_)

        secs = int(time.time() - start_tm)
        mins = secs / 60
        secs = secs % 60

        logger.info('Epoch: %d | time in %d minutes, %d seconds', epoch, mins, secs)
        logger.info('\tLoss: %.4f(train)\t|\tAcc %.1f(train)', train_loss, train_acc*100)
        logger.info('\tLoss: %.4f(valid)\t|\tAcc %.1f(valid)', valid_loss, valid_acc*100)
    logger.info('train finished')

    test_loss, test_acc = model_train.test(test_dataset)
    logger.info('\tLoss: %.4f(test)\t|\tAcc %.1f(test)', test_loss, test_acc*100)
    logger.info('test finished')
    logger.info('done')


if __name__ == '__main__':
    main()
