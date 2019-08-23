FROM python:3.7

RUN apt-get update && \
    apt-get install wget curl -y

COPY . /work/
WORKDIR /work
RUN pip install -r requirements.txt

CMD ["bash", "run.sh"]
