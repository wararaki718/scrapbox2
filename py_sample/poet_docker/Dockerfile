FROM python:3.8

RUN pip install poetry
COPY . /app

WORKDIR /app
RUN poetry config virtualenvs.create false && \
    poetry install

ENTRYPOINT [ "bash", "docker-entrypoint.sh" ]
