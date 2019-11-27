FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y curl unzip wget && \
    rm -rf /var/lib/apt/lists/*
COPY docker-entrypoint.sh /opt/docker-entrypoint.sh

ENTRYPOINT [ "/bin/bash", "/opt/docker-entrypoint.sh" ]
