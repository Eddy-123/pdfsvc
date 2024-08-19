FROM python:3.10-slim

RUN apt-get update
RUN apt-get -y install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0

WORKDIR /opt/pdfsvc

COPY ./pdfsvc .
COPY ./requirements.txt .

RUN pip install -r requirements.txt
