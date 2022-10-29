FROM debian:latest

USER root

WORKDIR /acre

RUN apt-get update -y
RUN apt-get install uuid-runtime
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y x11vnc xvfb daemon ffmpeg chromium-driver chromium sudo
RUN apt-get install -y rxvt dclock
RUN apt-get install -y git
RUN apt-get install -y procps


COPY bin/* /usr/local/bin/
COPY etc/init.d/xvfb /etc/init.d/
COPY etc/requirements.txt /usr/local/etc/

ARG ACRE_UPDATE_REQUIREMENTS
RUN python3 -m pip install -r /usr/local/etc/requirements.txt

RUN mkdir -p /tmp/installer
COPY installer/* /tmp/installer/

RUN /tmp/installer/tester-user.sh

USER tester

CMD ["idock"]

