FROM python:3.8

RUN apt-get update && apt-get install -y vim

COPY requirements.txt .
RUN pip3 install -r requirements.txt && rm requirements.txt
