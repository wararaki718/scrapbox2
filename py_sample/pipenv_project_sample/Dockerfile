FROM python:3.7

RUN pip install pipenv

WORKDIR /app
COPY . /app
RUN pipenv install

ENTRYPOINT ["bash", "docker-entrypoint.sh"]
