# sample pybind code

## setup

```shell
pip install pybind11
```

## build

```shell
c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup `python3 -m pybind11 --includes` example.cpp -o example`python3-config --extension-suffix`
```

## run

```shell
python main.py
```
