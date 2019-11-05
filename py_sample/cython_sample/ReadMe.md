# sample Cython

Pending

## setup environment

```shell
pip install Cython
```

## build

```shell
python setup.py install
```

## run

```shell
python main.py
```

## crean

```shell
python setup.py clean --all
```

## uninstall package

```shell
python setup.py install --record files.txt
cat files.txt | xargs rm -rf
rm files.txt
```
