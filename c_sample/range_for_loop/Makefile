CC = g++
CFLAGS = -std=c++11 -O2

.PHONY: all

all: main

main: main.cpp
	$(CC) $(CFLAGS) $(EIGEN_OPTION) -o main main.cpp

clean:
	rm main
