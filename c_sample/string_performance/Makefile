CC = g++
CFLAGS = -std=c++11 -O2

.PHONY: all

all: forward backward

forward: forward.cpp
	$(CC) $(CFLAGS) -o forward forward.cpp

backward: backward.cpp
	$(CC) $(CFLAGS) -o backward backward.cpp

clean:
	rm forward backward
