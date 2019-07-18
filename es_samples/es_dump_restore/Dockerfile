FROM docker.elastic.co/elasticsearch/elasticsearch:6.7.2

ARG SNAPSHOT_DIR=/var/lib/elasticsearch/snapshots

RUN mkdir -p ${SNAPSHOT_DIR}
RUN chown -R elasticsearch:elasticsearch ${SNAPSHOT_DIR}
