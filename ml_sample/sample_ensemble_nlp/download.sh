#!/bin/bash

poetry run kaggle datasets download -d rmisra/news-category-dataset
unzip news-category-dataset.zip -d sample_ensemble_nlp
rm news-category-dataset.zip

echo "finish to download data!"
