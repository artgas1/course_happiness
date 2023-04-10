FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y upgrade && \
    apt-get -y install python3.10 && \
    apt update && apt install python3-pip -y

# Method1 - installing LibreOffice and java
RUN apt-get --no-install-recommends install libreoffice -y
RUN apt-get install -y libreoffice-java-common

# Method2 - additionally installing unoconv
# RUN apt-get install unoconv

RUN apt-get install libpq-dev -y

ARG CACHEBUST=1
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apt install unoconv
# copy project
COPY . .