# Learning-to-rank by lightGBM on Python

## download dataset

```shell
bash download.sh
```

## setup environment

lightgbm

```shell
PIP_NO_CACHE_DIR=off PIP_NO_BINARY="lightgbm" pipenv install lightgbm
```

other libraries.

```shell
pipenv install scikit-learn scipy pandas
```

## run

```shell
pipenv run python learning-to-rank.py
```
