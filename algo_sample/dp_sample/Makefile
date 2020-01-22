CC = g++
CFLAGS = -std=c++11 -O2

.PHONY: all

all: full memo dp

full: full.cpp
	$(CC) $(CFLAGS) -o full full.cpp

memo: memo.cpp
	$(CC) $(CFLAGS) -o memo memo.cpp

dp: dp.cpp
	$(CC) $(CFLAGS) -o dp dp.cpp

clean:
	rm full memo dp
