FROM debian:10.5

USER root

WORKDIR /pantest

RUN apt-get update -y

# COPY bin/* /usr/local/bin
# RUN ls

ENTRYPOINT ["bin/dockerrun"]

