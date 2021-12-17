# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

COPY . /code

RUN  python -m pip install -r requirements.txt

COPY . /code/