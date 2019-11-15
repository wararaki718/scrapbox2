FROM python:3.7

WORKDIR /app
COPY . /app

RUN pip install pipenv

ARG BUILD_OPTION
RUN pipenv install ${BUILD_OPTION}

CMD [ "bash", "show-pkgs.sh" ]
