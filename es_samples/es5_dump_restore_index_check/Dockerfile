FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.0

# delete unsed plugin
RUN bin/elasticsearch-plugin remove x-pack --purge

ARG SNAPSHOT_DIR=/usr/share/elasticsearch/snapshots
RUN mkdir -p ${SNAPSHOT_DIR}
RUN echo "path.repo: [\"${SNAPSHOT_DIR}\"]" >> /usr/share/elasticsearch/config/elasticsearch.yml
