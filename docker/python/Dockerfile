FROM python:3.6

ENV PYTHONUNBUFFERED 1

ADD . /srv/www/project
WORKDIR /srv/www/project

RUN pip install -r requirements.txt