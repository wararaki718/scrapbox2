CC = g++
OPENMP_OPTION = -fopenmp

.PHONY: all

all: main

main: main.cpp
	$(CC) $(OPENMP_OPTION) -o main main.cpp

clean:
	rm main
