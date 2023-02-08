FROM python:3.11.1-slim-buster

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 4000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:4000"]


