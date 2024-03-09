FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /movieratings

RUN pip install --upgrade pip

COPY ./req.txt /movieratings/req.txt

RUN pip install -r req.txt

COPY . /movieratings/

EXPOSE 8000