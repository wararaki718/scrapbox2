FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y mysql-client && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /work
COPY run.sh /work/run.sh

CMD ["bash", "run.sh"]
