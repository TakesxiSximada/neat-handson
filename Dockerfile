# image: neat-handson
FROM ubuntu:jammy
MAINTAINER TakesxiSximada

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update -y && apt install -y  \
     git                              \
     fontconfig                        \
     python3-pip                        \
     python3-venv                        \
     language-pack-ja                     \
     fonts-noto-cjk-extra                  \
     fonts-noto-color-emoji

RUN git clone --depth 1 https://github.com/CodeReclaimers/neat-python.git
RUN pip install -e ./neat-python
