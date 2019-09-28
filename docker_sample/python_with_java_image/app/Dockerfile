FROM openjdk:8 as build_java

WORKDIR /build
COPY Sample.java /build
RUN javac Sample.java


FROM python:3.7

# install java & setup environment
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

WORKDIR /work
COPY . /work
COPY --from=build_java /build/Sample.class /work/

CMD ["bash", "docker-entrypoint.sh"]
