FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install unzip wget curl -y

COPY run.sh /work/run.sh
WORKDIR /work

CMD ["bash", "run.sh"]
