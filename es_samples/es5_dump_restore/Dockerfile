FROM elasticsearch:5.6

ARG SNAPSHOT_DIR=/usr/share/elasticsearch/snapshots
RUN mkdir -p ${SNAPSHOT_DIR}
RUN echo "path.repo: [\"${SNAPSHOT_DIR}\"]" >> /usr/share/elasticsearch/config/elasticsearch.yml
