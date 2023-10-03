FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip setuptools==57.5.0
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install sentry_sdk

COPY .. .

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]