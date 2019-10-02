# confirm a speed of the compile

## compile & check the speed

compile without options & check the compile speed.

```shell
time g++ -include all.h -o main main.cpp
# > g++ -include all.h -o main main.cpp  0.45s user 0.05s system 97% cpu 0.515 total
```

## compile with a precompile header

make a precompile header

```shell
g++ -x c++-header -o all.h.gch all.h
```

complie based on a precompile header & check the compile speed.

```shell
time g++ -include all.h -o main main.cpp
# > g++ -include all.h -o main main.cpp  0.10s user 0.05s system 93% cpu 0.159 total
```
