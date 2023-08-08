FROM python:3.8.13 -slim-buster
WORKDIR   /usr/src/app
ENV PYTHONDONTWRITEBYTECODE
ENV PYTHONUNBUFFERED

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app

RUN pip install -r requirements.txt

#copy project
COPY . /usr/src/app
EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]