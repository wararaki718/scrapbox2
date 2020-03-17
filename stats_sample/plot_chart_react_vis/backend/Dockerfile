FROM python:3.8

WORKDIR /backend
COPY . /backend

RUN pip install poetry
RUN poetry config virtualenvs.create false && \
    poetry install

EXPOSE 8000

ENTRYPOINT [ "bash", "docker-entrypoint.sh" ]
