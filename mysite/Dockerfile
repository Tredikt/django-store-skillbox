FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip setuptools==57.5.0
RUN pip install -r requirements.txt

COPY .. .

