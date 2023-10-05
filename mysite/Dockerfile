FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip setuptools==57.5.0 pip "poetry==1.4.2"

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

COPY .. .

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]