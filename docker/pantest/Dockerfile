FROM debian:latest

USER root

WORKDIR /pantest

RUN apt-get update -y
RUN apt-get install uuid-runtime
RUN apt-get install -y python3 python3-pip

RUN python3 -m pip install radish-bdd[bdd-xml]

COPY bin/* /usr/local/bin/

CMD ["idock"]

