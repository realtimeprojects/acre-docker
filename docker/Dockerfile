FROM debian:latest

USER root

WORKDIR /acre

RUN apt-get update -y
RUN apt-get install uuid-runtime
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y x11vnc xvfb daemon ffmpeg chromium-driver chromium sudo
RUN apt-get install -y rxvt dclock

RUN python3 -m pip install radish-bdd[bdd-xml] junit.xml lxml selenium

COPY bin/* /usr/local/bin/
COPY etc/init.d/xvfb /etc/init.d/
RUN mkdir -p /tmp/installer
COPY installer/* /tmp/installer/

RUN /tmp/installer/tester-user.sh

USER tester

CMD ["idock"]

