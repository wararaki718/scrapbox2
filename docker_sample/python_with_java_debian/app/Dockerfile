FROM openjdk:8 as build_java

WORKDIR /build
COPY Sample.java /build
RUN javac Sample.java


FROM python:3.7

# install java & setup environment
RUN apt-get update && \
    apt-get install -y default-jre && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /work
COPY . /work
COPY --from=build_java /build/Sample.class /work/

CMD ["bash", "docker-entrypoint.sh"]
