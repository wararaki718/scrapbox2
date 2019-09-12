FROM python:3.7

RUN apt-get update && \
    apt-get install wget curl -y

COPY . /work
WORKDIR /work

CMD ["bash", "run.sh"]
