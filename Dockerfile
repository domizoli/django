FROM python:3.10.11-slim-bullseye

ENV PYTHONBUFFERED=1

ENV PORT=8080

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONBUFFERED=1

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app/
