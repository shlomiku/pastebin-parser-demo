FROM python:3.6-slim

WORKDIR /opt/project
COPY ./requirements.txt ./

RUN apt-get update
RUN apt-get install -y iputils-ping

RUN pip install -r ./requirements.txt --default-timeout=200
