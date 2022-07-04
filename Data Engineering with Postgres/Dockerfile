FROM python:3.9.1

RUN apt-get update -y && apt-get upgrade -y

WORKDIR /modelling

COPY ./requirements.txt /modelling/requirements.txt

RUN pip install -r requirements.txt

COPY ./src /modelling/src