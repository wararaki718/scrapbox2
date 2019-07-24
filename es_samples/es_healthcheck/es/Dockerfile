FROM docker.elastic.co/elasticsearch/elasticsearch:6.7.2

# install plugin
RUN bin/elasticsearch-plugin install --batch repository-s3
RUN bin/elasticsearch-plugin install analysis-kuromoji
RUN bin/elasticsearch-plugin install analysis-icu
