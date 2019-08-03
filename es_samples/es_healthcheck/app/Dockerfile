FROM ubuntu:16.04

RUN apt update
RUN apt install -y curl

COPY check.sh /work/check.sh

WORKDIR /work
CMD ["/bin/bash", "check.sh"]
