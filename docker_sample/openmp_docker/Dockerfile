FROM ubuntu:18.04 as build-stage

RUN apt-get update && \
    apt-get install gcc g++ make libomp-dev -y && \
    rm -rf /var/lib/apt/lists/*

COPY main.cpp /build/main.cpp
COPY Makefile /build/Makefile

WORKDIR /build
RUN make

FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install libgomp1 -y && \
    rm -rf /var/lib/apt/lists/*

COPY --from=build-stage /build/main /work/main
WORKDIR /work

CMD ["./main"]
